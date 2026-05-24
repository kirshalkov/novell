from core.game_class import Game
from core.stage_init import init_stages
from list_stage import SCENES
from core.assets_load import assets_load
from core import core_config

stages = init_stages(SCENES)

def start_game(stage, screen, main_unit):
    return Game(
        stages=stages,
        screen=screen,
        stage=stages[stage],
        assets_loader=assets_load,
        base_width=core_config.BASE_WIDTH,
        base_height=core_config.BASE_HEIGHT,
        main_unit=main_unit,
    )
