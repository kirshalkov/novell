import pygame
import game_config
from core import core_config
from core import game_starter

pygame.init()
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)

clock = pygame.time.Clock()

game = game_starter.start_game(screen=screen, stage='start_menu', main_unit=game_config.main_unit)

# pygame.mixer.music.load("assets/music/main_theme.mp3")
# pygame.mixer.music.set_volume(0.4)
# pygame.mixer.music.play(-1)

while game.run:
    ui_data = game.draw_stage()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.run = False

        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            game.resize(screen)

        game.handle_load_menu(event, ui_data["load_menu_buttons"])
        game.handle_top_buttons(event, ui_data["top_buttons"])
        game.handle_answer_buttons(event, ui_data["answer_buttons"])

    pygame.display.flip()
    clock.tick(core_config.FPS)
