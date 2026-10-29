# CHECKPOINT 1: copy to main.py; read the visible input/update/draw loop.
from pathlib import Path
import pygame

def load_sprite(path, size):
    image = pygame.image.load(path).convert_alpha()
    return pygame.transform.smoothscale(image, (size, size))



def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Robot docking - arrow keys move")
    clock = pygame.time.Clock()
    images = Path(__file__).resolve().parent / "images"
    #robot_image = pygame.image.load(images / "robot.png").convert_alpha()
    #robot_image = pygame.transform.smoothscale(robot_image, (64, 64))
    sprites = {
        "up" : load_sprite( images / "robot_up.png", 64),
        "right": load_sprite(images / "robot_right.png", 64),
        "left": load_sprite(images / "robot_left.png", 64),
        "down": load_sprite(images / "robot_down.png", 64),
    }
    pad = pygame.image.load(images / "landing_pad.png").convert_alpha()
    pad = pygame.transform.smoothscale(pad, (96, 96))
    t, r = 640,300
    pad_position = (t, r)
    x, y = 160.0, 300.0
    speed = 180
    running = True
    touching = False

    facing = "up"
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
        x += dx * speed * dt
        y += dy * speed * dt
        x = max(32, min(768, x))
        y = max(32, min(568, y))

        screen.fill("#DDF2FF")
        pygame.draw.rect(screen, "#95C549", (0, 420, 800, 180))
        pygame.draw.rect(screen, "#F7D34B", (80, 390, 640, 18))

        if dy>0:
            facing = "down"
        
        
        rectangle = sprites[facing].get_rect(center=(round(x), round(y)))
        screen.blit(sprites[facing], rectangle)

        # check touching
        touching=abs(x-t) < 48 and abs(y-r) < 48
        if not touching:
            screen.blit(pad, pad.get_rect(center=pad_position))
            
        
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
