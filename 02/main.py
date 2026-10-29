# LESSON 02 / CHECKPOINT 3: one file, one Player object.
# Supplied setup is visible. No studio.py.
from pathlib import Path
import pygame

def load_sprite(path, size):
    image = pygame.image.load(path).convert_alpha()
    return pygame.transform.smoothscale(image, (size, size))


def draw_scene(screen, pad, pad_position):
    screen.fill("#DDF2FF")
    pygame.draw.rect(screen, "#95C549", (0, 420, 800, 180))
    pygame.draw.rect(screen, "#F7D34B", (80, 390, 640, 18))
    screen.blit(pad, pad.get_rect(center=pad_position))


class Player:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.speed = 180
        self.image = image

    def move(self, dx, dy, dt):
        self.x += dx * self.speed * dt
        self.y += dy * self.speed * dt
        self.x = max(32, min(768, self.x))
        self.y = max(32, min(568, self.y))

    def draw(self, screen):
        rectangle = self.image.get_rect(center=(round(self.x), round(self.y)))
        screen.blit(self.image, rectangle)


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Robot docking - arrow keys move")
    clock = pygame.time.Clock()
    images = Path(__file__).resolve().parent / "images"
    robot_image = load_sprite(images / "robot.png", 64)
    pad = load_sprite(images / "landing_pad.png", 96)
    pad_position = (640, 300)
    player = Player(160, 300, robot_image)
    running = True

    while running:
        dt = min(clock.tick(60) / 1000, 0.05)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx = -1
        if keys[pygame.K_RIGHT]:
            dx = 1
        if keys[pygame.K_UP]:
            dy = -1
        if keys[pygame.K_DOWN]:
            dy = 1
        player.move(dx, dy, dt)

        draw_scene(screen, pad, pad_position)
        player.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
