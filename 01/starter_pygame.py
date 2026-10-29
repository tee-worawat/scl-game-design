import pygame
from pathlib import Path

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

x, y = 160, 300
speed = 180  # Pixels per second
ROOT = Path(__file__).resolve().parent


def update(dt):
    global x

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        x += speed * dt
    if keys[pygame.K_LEFT]:
        x -= speed * dt

    x = max(24, min(776, x))


def draw():
    screen.fill("#eef3fc")  # Clear the previous frame
    pygame.draw.circle(screen, "#294fc4", (round(x), y), 24)
    # image = pygame.image.load(ROOT / 'images' / ('robot' + '.png')).convert_alpha()
    # image = pygame.transform.scale(image, (100,100))
    # screen.blit(image, image.get_rect(center=(round(160), round(300))))


def run():
    running = True

    while running:
        dt = min(clock.tick(60) / 1000, 0.05)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not running:
            break

        update(dt)             # Change the game state
        draw()                 # Draw the current state
        pygame.display.flip()  # Show the finished frame

    pygame.quit()


if __name__ == "__main__":
    run()