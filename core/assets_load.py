import pygame
from core.core_config import error_png
from pathlib import Path

def assets_load(path, scale_global, scale_local=1, bg=False):

    if not path.exists():
        print(f'!Не найден ассет: {path}')
        path = Path(error_png)

    image = pygame.image.load(str(path))
    image = image.convert_alpha() if not bg else image.convert()

    orig_w, orig_h = image.get_size()
    new_w = int(orig_w * scale_global * scale_local)
    new_h = int(orig_h * scale_global * scale_local)

    return pygame.transform.smoothscale(image, (new_w, new_h))
