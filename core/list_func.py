import random

def new_stage(game, stage_new):
    game.start_scene_transition(stage_new)

def new_stage_rng(game, stage_new_1, stage_new_2, rng_1):
    stage_new = (stage_new_1, stage_new_2)[random.randint(0, 100) < rng_1]
    game.start_scene_transition(stage_new)

# rng число от 1 до 99, если выпадет меньше, то будет первая сцена