import pygame
from pathlib import Path

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Robot docking - arrow keys move")
clock = pygame.time.Clock()
images = Path(__file__).resolve().parent / "images"
#robot_image_path = (images / "robot.png", 64)
robot_image = pygame.image.load(images / "robot.png").convert_alpha()
robot_image = pygame.transform.smoothscale(robot_image, (64, 64))
pad = pygame.image.load(images / "landing_pad.png").convert_alpha()
pad = pygame.transform.smoothscale(pad, (64,64))
pad_position = (640, 300)
robot_position = (160,300)
x,y = 160, 300
speed = 180
running = True

while running:
    dt = min(clock.tick(60) / 1000, 0.05)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    keys = pygame.key.get_pressed() # Key events 
    dy = 0 
    if keys[pygame.K_UP]:
        dy = -30
    y = y + dy
    screen.fill("#DDF2FF")
    pygame.draw.rect(screen, "#95C549", (0, 420, 800, 180))
    pygame.draw.rect(screen, "#F7D34B", (80, 390, 640, 18))
    screen.blit(robot_image, robot_image.get_rect(center=(x,y)))
    screen.blit(pad, pad.get_rect(center=pad_position))
    
    pygame.display.flip()

pygame.quit()
