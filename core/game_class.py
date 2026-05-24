import json
import math
from datetime import datetime
from pathlib import Path

import pygame
from core import UI_config


class Game:
    def __init__(self, screen, stage, assets_loader, base_width, base_height, stages, main_unit):
        self.screen = screen
        self.stage = stage
        self.assets_loader = assets_loader
        self.base_width = base_width
        self.base_height = base_height

        self.scale = 1
        self.bg = None
        self.unit = None
        self.unit_base_image = None

        self.run = True
        self.stages = stages
        self.main_unit = main_unit
        self.stage_name = self._find_stage_name(stage)

        # анимация перехода сцен
        self.transition_active = False
        self.transition_alpha = 0
        self.transition_phase = None
        self.transition_target = None

        # сохранения
        self.saves_dir = Path("saves")
        self.saves_dir.mkdir(exist_ok=True)
        self.load_menu_open = False
        self.active_popup_message = ""
        self.popup_message_until = 0

        # анимация текста
        self.text_visible_chars = 0.0
        self.last_text_update_ticks = pygame.time.get_ticks()

        # анимация кнопок
        self.button_scales = {}

        self.update_scale()
        self.reload_stage_assets()
        self.reset_text_animation()

    def _find_stage_name(self, stage_obj):
        for name, stage in self.stages.items():
            if stage is stage_obj:
                return name
        return None

    def update_scale(self):
        screen_w, screen_h = self.screen.get_size()
        scale_x = screen_w / self.base_width
        scale_y = screen_h / self.base_height
        self.scale = min(scale_x, scale_y)

    def reload_stage_assets(self):
        bg_raw = self.assets_loader(self.stage.bg, 1, bg=True)
        self.bg = pygame.transform.smoothscale(bg_raw, self.screen.get_size())

        if self.stage.unit is not None:
            self.unit_base_image = self.assets_loader(
                self.stage.unit,
                self.scale,
                self.stage.scale_unit
            )
            self.unit = self.unit_base_image
        else:
            self.unit_base_image = None
            self.unit = None

    def resize(self, new_screen):
        self.screen = new_screen
        self.update_scale()
        self.reload_stage_assets()

    def stage_update(self, stage_new, stage_name=None):
        self.stage = stage_new
        self.stage_name = stage_name or self._find_stage_name(stage_new)
        self.reload_stage_assets()
        self.reset_text_animation()

    def reset_text_animation(self):
        initial_chars = getattr(UI_config, "TEXT_TYPING_INITIAL_CHARS", 0)
        self.text_visible_chars = max(0.0, float(initial_chars))
        self.last_text_update_ticks = pygame.time.get_ticks()

    def finish_text_animation(self):
        self.text_visible_chars = float(len(self.stage.text))
        self.last_text_update_ticks = pygame.time.get_ticks()

    def is_text_fully_visible(self):
        return int(self.text_visible_chars) >= len(self.stage.text)

    def update_text_animation(self):
        if not getattr(UI_config, "TEXT_TYPING_ENABLED", True):
            self.text_visible_chars = float(len(self.stage.text))
            return

        if self.is_text_fully_visible():
            return

        now = pygame.time.get_ticks()
        delta_ms = now - self.last_text_update_ticks
        self.last_text_update_ticks = now

        speed = max(1, getattr(UI_config, "TEXT_TYPING_SPEED", 45))
        self.text_visible_chars += speed * (delta_ms / 1000.0)
        if self.text_visible_chars > len(self.stage.text):
            self.text_visible_chars = float(len(self.stage.text))

    def get_visible_stage_text(self):
        if not getattr(UI_config, "TEXT_TYPING_ENABLED", True):
            return self.stage.text
        return self.stage.text[:int(self.text_visible_chars)]

    def wrap_text(self, text, font, max_width):
        words = text.split()
        lines = []
        current_line = ""

        for word in words:
            test_line = word if current_line == "" else current_line + " " + word

            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)
                current_line = word

        if current_line:
            lines.append(current_line)

        return lines

    def lighten_color(self, color, amount):
        return tuple(min(255, c + amount) for c in color)

    def show_popup(self, message, duration_ms=1800):
        self.active_popup_message = message
        self.popup_message_until = pygame.time.get_ticks() + duration_ms

    def _update_button_scale(self, button_key, is_hover):
        target = getattr(UI_config, "BUTTON_HOVER_SCALE", 1.08) if is_hover else 1.0
        current = self.button_scales.get(button_key, 1.0)
        speed = getattr(UI_config, "BUTTON_ANIMATION_SPEED", 0.22)
        current += (target - current) * speed
        self.button_scales[button_key] = current
        return current

    def _draw_animated_button(self, rect, text_surf, text_color, base_color, border_color,
                              border_radius, border_width, is_hover, button_key):
        scale_factor = self._update_button_scale(button_key, is_hover)
        color = self.lighten_color(base_color, getattr(UI_config, "BUTTON_HOVER_LIGHTEN", 35)) if is_hover else base_color

        animated_rect = pygame.Rect(0, 0, max(1, int(rect.width * scale_factor)), max(1, int(rect.height * scale_factor)))
        animated_rect.center = rect.center

        pygame.draw.rect(self.screen, color, animated_rect, border_radius=max(1, int(border_radius * scale_factor)))
        pygame.draw.rect(
            self.screen,
            border_color,
            animated_rect,
            width=border_width,
            border_radius=max(1, int(border_radius * scale_factor))
        )

        text_x = animated_rect.x + (animated_rect.width - text_surf.get_width()) // 2
        text_y = animated_rect.y + (animated_rect.height - text_surf.get_height()) // 2
        self.screen.blit(text_surf, (text_x, text_y))
        return animated_rect

    def draw_answer_buttons(self):
        if not self.stage.vars_return:
            return []

        scale_ui = self.scale
        screen_w, _ = self.screen.get_size()
        mouse_pos = pygame.mouse.get_pos()

        button_font = pygame.font.SysFont("arial", max(14, int(22 * scale_ui)))

        padding_x = int(18 * scale_ui)
        padding_y = int(10 * scale_ui)
        margin_top = int(25 * scale_ui)
        margin_right = int(25 * scale_ui)
        spacing = int(12 * scale_ui)
        border_radius = int(12 * scale_ui)
        border_width = max(1, int(2 * scale_ui))

        base_color = (55, 55, 55)
        border_color = (220, 220, 220)
        text_color = (245, 245, 245)

        max_text_width = 0
        text_surfaces = []

        for var in self.stage.vars_return:
            text_surf = button_font.render(var.text, True, text_color)
            text_surfaces.append(text_surf)
            max_text_width = max(max_text_width, text_surf.get_width())

        button_w = max_text_width + padding_x * 2

        button_data = []
        current_y = margin_top

        for index, (var, text_surf) in enumerate(zip(self.stage.vars_return, text_surfaces)):
            button_h = text_surf.get_height() + padding_y * 2
            button_x = screen_w - margin_right - button_w

            rect = pygame.Rect(button_x, current_y, button_w, button_h)
            is_hover = rect.collidepoint(mouse_pos)
            animated_rect = self._draw_animated_button(
                rect=rect,
                text_surf=text_surf,
                text_color=text_color,
                base_color=base_color,
                border_color=border_color,
                border_radius=border_radius,
                border_width=border_width,
                is_hover=is_hover,
                button_key=f"answer_{self.stage_name}_{index}",
            )

            button_data.append((animated_rect, var))
            current_y += button_h + spacing

        return button_data

    def draw_top_buttons(self):
        scale_ui = self.scale
        mouse_pos = pygame.mouse.get_pos()
        font = pygame.font.SysFont("arial", max(14, int(20 * scale_ui)), bold=True)

        padding_x = int(16 * scale_ui)
        padding_y = int(10 * scale_ui)
        margin_left = int(20 * scale_ui)
        margin_top = int(20 * scale_ui)
        spacing = int(12 * scale_ui)
        border_radius = int(12 * scale_ui)
        border_width = max(1, int(2 * scale_ui))

        labels = [
            ("save", "Сохранить"),
            ("load", "Загрузить"),
        ]

        button_data = []
        current_x = margin_left

        for button_id, label in labels:
            text_surf = font.render(label, True, (245, 245, 245))
            button_w = text_surf.get_width() + padding_x * 2
            button_h = text_surf.get_height() + padding_y * 2
            rect = pygame.Rect(current_x, margin_top, button_w, button_h)
            is_hover = rect.collidepoint(mouse_pos)

            animated_rect = self._draw_animated_button(
                rect=rect,
                text_surf=text_surf,
                text_color=(245, 245, 245),
                base_color=(45, 45, 45),
                border_color=(220, 220, 220),
                border_radius=border_radius,
                border_width=border_width,
                is_hover=is_hover,
                button_key=f"top_{button_id}",
            )

            button_data.append((animated_rect, button_id))
            current_x += button_w + spacing

        return button_data

    def get_save_data(self):
        return {
            'stage_name': self.stage_name,
            'main_unit': self.main_unit,
            'saved_at': datetime.now().isoformat(timespec='seconds'),
        }

    def get_save_files(self):
        save_files = []

        for path in sorted(self.saves_dir.glob("*.json"), reverse=True):
            try:
                with path.open("r", encoding="utf-8") as file:
                    data = json.load(file)
                save_files.append({
                    "path": path,
                    "file_name": path.name,
                    "stage_name": data.get("stage_name", "неизвестно"),
                    "saved_at": data.get("saved_at", "без даты"),
                })
            except (OSError, json.JSONDecodeError):
                save_files.append({
                    "path": path,
                    "file_name": path.name,
                    "stage_name": "повреждено",
                    "saved_at": "не удалось прочитать",
                })

        return save_files

    def save_game(self):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        save_path = self.saves_dir / f"save_{timestamp}.json"

        with save_path.open("w", encoding="utf-8") as file:
            json.dump(self.get_save_data(), file, ensure_ascii=False, indent=4)

        self.show_popup(f"Сохранено: {save_path.name}")

    def load_game(self, save_path):
        try:
            with Path(save_path).open("r", encoding="utf-8") as file:
                data = json.load(file)
        except (OSError, json.JSONDecodeError):
            self.show_popup("Не удалось загрузить сохранение")
            return

        stage_name = data.get("stage_name")
        if stage_name not in self.stages:
            self.show_popup("Сцена из сохранения не найдена")
            return

        self.main_unit = data.get("main_unit", self.main_unit)
        self.load_menu_open = False
        self.start_scene_transition(stage_name)
        self.show_popup(f"Загружено: {Path(save_path).name}")

    def start_scene_transition(self, stage_name):
        if self.transition_active:
            return

        if stage_name not in self.stages:
            return

        self.transition_active = True
        self.transition_alpha = 0
        self.transition_phase = 'out'
        self.transition_target = stage_name

    def update_scene_transition(self):
        if not self.transition_active:
            return

        speed = getattr(UI_config, "TRANSITION_SPEED", 15)

        if self.transition_phase == 'out':
            self.transition_alpha += speed

            if self.transition_alpha >= 255:
                self.transition_alpha = 255
                self.stage_update(self.stages[self.transition_target], self.transition_target)
                self.transition_phase = 'in'

        elif self.transition_phase == 'in':
            self.transition_alpha -= speed

            if self.transition_alpha <= 0:
                self.transition_alpha = 0
                self.transition_active = False
                self.transition_phase = None
                self.transition_target = None

    def draw_scene_transition(self):
        if not self.transition_active:
            return

        transition_color = getattr(UI_config, "TRANSITION_COLOR", (0, 0, 0))

        overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        r, g, b = transition_color
        overlay.fill((r, g, b, self.transition_alpha))
        self.screen.blit(overlay, (0, 0))

    def draw_load_menu(self):
        if not self.load_menu_open:
            return []

        scale_ui = self.scale
        screen_w, screen_h = self.screen.get_size()
        mouse_pos = pygame.mouse.get_pos()

        overlay = pygame.Surface((screen_w, screen_h), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 170))
        self.screen.blit(overlay, (0, 0))

        panel_w = int(screen_w * 0.7)
        panel_h = int(screen_h * 0.72)
        panel_x = (screen_w - panel_w) // 2
        panel_y = (screen_h - panel_h) // 2
        panel_rect = pygame.Rect(panel_x, panel_y, panel_w, panel_h)

        pygame.draw.rect(self.screen, (28, 28, 28), panel_rect, border_radius=int(18 * scale_ui))
        pygame.draw.rect(
            self.screen,
            (220, 220, 220),
            panel_rect,
            width=max(1, int(2 * scale_ui)),
            border_radius=int(18 * scale_ui)
        )

        title_font = pygame.font.SysFont("arial", max(18, int(28 * scale_ui)), bold=True)
        item_font = pygame.font.SysFont("arial", max(14, int(20 * scale_ui)))
        small_font = pygame.font.SysFont("arial", max(12, int(16 * scale_ui)))

        title_surf = title_font.render("Меню сохранений", True, (245, 245, 245))
        self.screen.blit(title_surf, (panel_x + int(24 * scale_ui), panel_y + int(20 * scale_ui)))

        close_text = title_font.render("×", True, (245, 245, 245))
        close_rect = close_text.get_rect()
        close_rect.topright = (panel_x + panel_w - int(24 * scale_ui), panel_y + int(18 * scale_ui))
        self.screen.blit(close_text, close_rect)

        save_entries = self.get_save_files()
        buttons = [(close_rect.inflate(16, 10), ("close_menu", None))]

        list_x = panel_x + int(24 * scale_ui)
        list_y = panel_y + int(80 * scale_ui)
        list_w = panel_w - int(48 * scale_ui)
        item_h = int(72 * scale_ui)
        spacing = int(10 * scale_ui)

        if not save_entries:
            empty_surf = item_font.render("Сохранений пока нет", True, (220, 220, 220))
            self.screen.blit(empty_surf, (list_x, list_y))
            return buttons

        for index, save_info in enumerate(save_entries):
            item_y = list_y + index * (item_h + spacing)
            if item_y + item_h > panel_y + panel_h - int(20 * scale_ui):
                break

            rect = pygame.Rect(list_x, item_y, list_w, item_h)
            is_hover = rect.collidepoint(mouse_pos)
            color = (75, 75, 75) if is_hover else (55, 55, 55)

            pygame.draw.rect(self.screen, color, rect, border_radius=int(12 * scale_ui))
            pygame.draw.rect(
                self.screen,
                (180, 180, 180),
                rect,
                width=max(1, int(1 * scale_ui)),
                border_radius=int(12 * scale_ui)
            )

            name_text = f"{save_info['file_name']}"
            info_text = f"Сцена: {save_info['stage_name']}"
            date_text = f"Дата: {save_info['saved_at']}"

            self.screen.blit(item_font.render(name_text, True, (245, 245, 245)), (rect.x + int(16 * scale_ui), rect.y + int(10 * scale_ui)))
            self.screen.blit(small_font.render(info_text, True, (225, 225, 225)), (rect.x + int(16 * scale_ui), rect.y + int(38 * scale_ui)))
            self.screen.blit(small_font.render(date_text, True, (200, 200, 200)), (rect.x + int(list_w * 0.48), rect.y + int(38 * scale_ui)))

            buttons.append((rect, ("load_save", save_info["path"])))

        return buttons

    def draw_popup(self):
        if not self.active_popup_message:
            return

        if pygame.time.get_ticks() > self.popup_message_until:
            self.active_popup_message = ""
            return

        scale_ui = self.scale
        font = pygame.font.SysFont("arial", max(14, int(20 * scale_ui)), bold=True)
        text_surf = font.render(self.active_popup_message, True, (245, 245, 245))

        padding_x = int(16 * scale_ui)
        padding_y = int(10 * scale_ui)
        box_w = text_surf.get_width() + padding_x * 2
        box_h = text_surf.get_height() + padding_y * 2
        box_x = (self.screen.get_width() - box_w) // 2
        box_y = int(18 * scale_ui)

        rect = pygame.Rect(box_x, box_y, box_w, box_h)
        pygame.draw.rect(self.screen, (35, 35, 35), rect, border_radius=int(12 * scale_ui))
        pygame.draw.rect(self.screen, (220, 220, 220), rect, width=max(1, int(2 * scale_ui)), border_radius=int(12 * scale_ui))
        self.screen.blit(text_surf, (box_x + padding_x, box_y + padding_y))

    def handle_top_buttons(self, event, button_data):
        if event.type != pygame.MOUSEBUTTONDOWN or event.button != 1:
            return

        for rect, button_id in button_data:
            if rect.collidepoint(event.pos):
                if button_id == "save":
                    self.save_game()
                elif button_id == "load":
                    self.load_menu_open = True
                return

    def handle_load_menu(self, event, button_data):
        if not self.load_menu_open:
            return

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.load_menu_open = False
            return

        if event.type != pygame.MOUSEBUTTONDOWN or event.button != 1:
            return

        for rect, action in button_data:
            if rect.collidepoint(event.pos):
                action_name, payload = action
                if action_name == "close_menu":
                    self.load_menu_open = False
                elif action_name == "load_save":
                    self.load_game(payload)
                return

        self.load_menu_open = False

    def handle_answer_buttons(self, event, button_data):
        if self.transition_active or self.load_menu_open:
            return

        if event.type != pygame.MOUSEBUTTONDOWN:
            return

        if event.button != 1:
            return

        for rect, var in button_data:
            if rect.collidepoint(event.pos):
                if not self.is_text_fully_visible():
                    self.finish_text_animation()
                    return

                func = var.func
                args = var.args

                if func is None:
                    return

                if args is None:
                    func(self)
                elif isinstance(args, (tuple, list)):
                    func(self, *args)
                else:
                    func(self, args)

                return

    def get_speaker_name(self):
        if self.stage.name_unit is None:
            return ""
        return str(self.stage.name_unit)

    def _get_unit_draw_data(self):
        if not self.unit_base_image:
            return None, 0, 0

        image = self.unit_base_image
        y_offset = 0

        if getattr(UI_config, "UNIT_BREATH_ENABLED", True):
            ticks = pygame.time.get_ticks()
            phase = ticks * getattr(UI_config, "UNIT_BREATH_SPEED", 0.0032)
            y_offset = math.sin(phase) * getattr(UI_config, "UNIT_BREATH_Y_AMPLITUDE", 6) * self.scale
            scale_delta = 1 + math.sin(phase) * getattr(UI_config, "UNIT_BREATH_SCALE_AMPLITUDE", 0.025)

            new_w = max(1, int(self.unit_base_image.get_width() * scale_delta))
            new_h = max(1, int(self.unit_base_image.get_height() * scale_delta))
            image = pygame.transform.smoothscale(self.unit_base_image, (new_w, new_h))

        return image, 0, int(y_offset)

    def draw_stage(self):
        self.update_scene_transition()
        self.update_text_animation()

        scale_ui = self.scale
        screen_w, screen_h = self.screen.get_size()

        self.screen.fill((0, 0, 0))

        if self.bg:
            self.screen.blit(self.bg, (0, 0))

        if self.unit:
            unit_image, _, breath_y = self._get_unit_draw_data()
            unit_x = int(100 - self.stage.unit_offset_x * scale_ui)
            unit_y = int(120 - self.stage.unit_offset_y * scale_ui) + breath_y
            if unit_image is not None:
                draw_x = unit_x - (unit_image.get_width() - self.unit_base_image.get_width()) // 2
                draw_y = unit_y - (unit_image.get_height() - self.unit_base_image.get_height()) // 2
                self.screen.blit(unit_image, (draw_x, draw_y))

        dialog_x = int(40 * scale_ui)
        dialog_y = int(screen_h - 260 * scale_ui)
        dialog_w = int(screen_w - 80 * scale_ui)
        dialog_h = int(220 * scale_ui)

        border_radius = int(18 * scale_ui)
        border_width = max(1, int(3 * scale_ui))
        padding = int(20 * scale_ui)

        dialog_surface = pygame.Surface((dialog_w, dialog_h), pygame.SRCALPHA)
        dialog_surface.fill((20, 20, 20, 190))
        self.screen.blit(dialog_surface, (dialog_x, dialog_y))

        pygame.draw.rect(
            self.screen,
            (230, 230, 230),
            pygame.Rect(dialog_x, dialog_y, dialog_w, dialog_h),
            width=border_width,
            border_radius=border_radius
        )

        speaker_name = self.get_speaker_name()
        if speaker_name:
            name_font = pygame.font.SysFont("arial", max(18, int(26 * scale_ui)), bold=True)
            name_surf = name_font.render(speaker_name, True, (255, 230, 170))
            self.screen.blit(name_surf, (dialog_x + padding, dialog_y + int(14 * scale_ui)))
            text_top = dialog_y + int(52 * scale_ui)
        else:
            text_top = dialog_y + int(22 * scale_ui)

        text_font = pygame.font.SysFont("arial", max(18, int(26 * scale_ui)))
        visible_text = self.get_visible_stage_text()
        lines = self.wrap_text(visible_text, text_font, dialog_w - padding * 2)

        line_height = text_font.get_linesize() + int(4 * scale_ui)
        for index, line in enumerate(lines[:6]):
            text_surf = text_font.render(line, True, (245, 245, 245))
            self.screen.blit(text_surf, (dialog_x + padding, text_top + index * line_height))

        top_buttons = self.draw_top_buttons()
        answer_buttons = self.draw_answer_buttons()
        load_menu_buttons = self.draw_load_menu()

        self.draw_scene_transition()
        self.draw_popup()

        return {
            "top_buttons": top_buttons,
            "answer_buttons": answer_buttons,
            "load_menu_buttons": load_menu_buttons,
        }
