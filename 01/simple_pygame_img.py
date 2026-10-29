from pathlib import Path
import pygame

pygame.init()
from pathlib import Path
ROOT = Path(__file__).resolve().parent

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Move your sprite!")
clock = pygame.time.Clock()
screen.fill("#9fbbee")
# Load the image from the same folder as this file.
player = pygame.image.load(ROOT / 'images' / ('robot' + '.png')).convert_alpha()
#player = pygame.image.load(image).convert_alpha()
player = pygame.transform.smoothscale(player, (64, 64))

x, y = 400.0, 300.0
speed = 180  # Pixels per second
running = True

while running:
    dt = clock.tick(60) / 1000  # Seconds since the last frame

    # 1. Handle closing the window.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Move the sprite while an arrow key is held.
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed * dt
    if keys[pygame.K_RIGHT]:
        x += speed * dt
    if keys[pygame.K_UP]:
        y -= speed * dt
    if keys[pygame.K_DOWN]:
        y += speed * dt

    # Keep the sprite inside the window.
    x = max(32, min(768, x))
    y = max(32, min(568, y))

    # 3. Clear the old frame and draw the new one.
    screen.fill("#EDF2FF")
    player_rect = player.get_rect(center=(round(x), round(y)))
    screen.blit(player, player_rect)
    pygame.display.flip()

pygame.quit()