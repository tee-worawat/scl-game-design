"""Teacher-provided Pygame support. Readable source; not a separate game engine.
Owns window, events, elapsed time, image loading, and text drawing.
Learners own game rules in starter.py. Images are scaled only while rendering.
"""
from pathlib import Path
import os
import pygame

WIDTH, HEIGHT = 800, 600
screen = None
_keys = set()
_cache = {}
ROOT = Path(__file__).resolve().parent


def held(name):
    return name in _keys


def background():
    screen.fill('#101d35')
    for x in range(0, WIDTH, 40):
        pygame.draw.line(screen, '#1a2b49', (x, 70), (x, HEIGHT))
    for y in range(80, HEIGHT, 40):
        pygame.draw.line(screen, '#1a2b49', (0, y), (WIDTH, y))


def picture(name, x, y, size=64):
    """Center a sprite at (x,y). Fit its visible artwork inside size pixels."""
    key = (name, size)
    if key not in _cache:
        original = pygame.image.load(ROOT / 'images' / (name + '.png')).convert_alpha()
        bounds = original.get_bounding_rect()
        visible = original.subsurface(bounds)  # runtime view; source PNG stays unchanged
        factor = size / max(visible.get_size())
        _cache[key] = pygame.transform.smoothscale(visible, (max(1, round(visible.get_width()*factor)), max(1, round(visible.get_height()*factor))))
    image = _cache[key]
    screen.blit(image, image.get_rect(center=(round(x), round(y))))


def text(message, x, y, size=24, color='white'):
    font_path = ROOT / 'fonts' / 'LINESeedSans_Rg.ttf'
    font = pygame.font.Font(str(font_path), size)
    screen.blit(font.render(str(message), True, color), (x, y))


def touching(ax, ay, bx, by):
    """A deliberately simple, visible 48×48 rectangular hitbox per object."""
    return abs(ax-bx) < 48 and abs(ay-by) < 48


def hitbox(x, y):
    pygame.draw.rect(screen, '#f8d348', (x-24, y-24, 48, 48), 1)


def run(namespace):
    global screen, _keys
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Spark · Game Designer')
    clock = pygame.time.Clock()
    frames = 0
    limit = int(os.environ.get('SPARK_SMOKE_FRAMES', '0'))
    alive = True
    while alive:
        dt = min(clock.tick(60) / 1000, 0.05)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                alive = False
            elif event.type == pygame.KEYDOWN:
                name = pygame.key.name(event.key)
                if name == 'escape':
                    alive = False
                if 'on_key' in namespace:
                    namespace['on_key'](name)
        pressed = pygame.key.get_pressed()
        _keys = {name for name, key in [('left', pygame.K_LEFT), ('right', pygame.K_RIGHT), ('up', pygame.K_UP), ('down', pygame.K_DOWN)] if pressed[key]}
        if 'update' in namespace:
            namespace['update'](dt)
        namespace['draw']()
        if pressed[pygame.K_h]:
            hitbox(namespace.get('x', 120), namespace.get('y', 300))
        pygame.display.flip()
        frames += 1
        if limit and frames >= limit:
            alive = False
    pygame.quit()
