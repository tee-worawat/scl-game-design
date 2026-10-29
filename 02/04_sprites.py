# LESSON 02 / CHECKPOINT 5: top-down directional sprites.
# A sprite is a drawable game image; pygame.sprite.Sprite is not required.
# Supplied setup is visible. No studio.py.
from pathlib import Path
import pygame

def load_sprite(path, size):
    image = pygame.image.load(path).convert_alpha()
    return pygame.transform.smoothscale(image, (size, size))


def draw_scene(screen, pad, pad_position):
    screen.fill("#DDF2FF")
    # A floor seen from above: no sky, horizon or side-on ground.
    for x in range(0, 800, 80):
        pygame.draw.line(screen, "#BDD9E8", (x, 0), (x, 600))
    for y in range(0, 600, 80):
        pygame.draw.line(screen, "#BDD9E8", (0, y), (800, y))
    pygame.draw.rect(screen, "#F7D34B", (80, 275, 640, 50))
    screen.blit(pad, pad.get_rect(center=pad_position))


class Player:
    def __init__(self, x, y, sprites):
        self.x = x
        self.y = y
        self.speed = 180
        self.sprites = sprites
        self.facing = "down"

    def move(self, dx, dy, dt):
        # Vertical wins on a diagonal. No input keeps the previous direction.
        if dy < 0:
            self.facing = "up"
        elif dy > 0:
            self.facing = "down"
        elif dx < 0:
            self.facing = "left"
        elif dx > 0:
            self.facing = "right"

        self.x += dx * self.speed * dt
        self.y += dy * self.speed * dt
        self.x = max(32, min(768, self.x))
        self.y = max(32, min(568, self.y))

    def draw(self, screen):
        image = self.sprites[self.facing]
        rectangle = image.get_rect(center=(round(self.x), round(self.y)))
        screen.blit(image, rectangle)


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Robot docking - arrow keys move")
    clock = pygame.time.Clock()
    images = Path(__file__).resolve().parent / "images"
    # A dictionary pairs a direction name (key) with its loaded picture (value).
    # Load once, outside the loop. All frames use the same 64px canvas/centre.
    sprites = {
        "up": load_sprite(images / "robot_up.png", 64),
        "right": load_sprite(images / "robot_right.png", 64),
        "down": load_sprite(images / "robot_down.png", 64),
        "left": load_sprite(images / "robot_left.png", 64),
    }
    pad = load_sprite(images / "landing_pad.png", 96)
    pad_position = (640, 300)
    player = Player(160, 300, sprites)
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
