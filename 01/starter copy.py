# Game Designer · Lesson 01
# Read before running. Arrow keys move (lesson 2+); R resets (lesson 4+); Esc quits.
# studio.py handles the window and graphics; this file owns the game rules.
import studio as g

from pathlib import Path
import os
import pygame

x = 160
y = 300

WIDTH, HEIGHT = 800, 600
screen = None
_keys = set()
_cache = {}
ROOT = Path(__file__).resolve().parent

def background():
    screen.fill('#101d35')
    for x in range(0, WIDTH, 40):
        pygame.draw.line(screen, '#1a2b49', (x, 70), (x, HEIGHT))
    for y in range(80, HEIGHT, 40):
        pygame.draw.line(screen, '#1a2b49', (0, y), (WIDTH, y))


def draw():
    g.background()
    g.picture('robot', x, y)
    g.text('Mission 1: place your robot', 24, 20)

if __name__ == '__main__':
    
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    
    pygame.display.set_caption('Spark · Game Designer')
    clock = pygame.time.Clock()
    frames = 0
    limit = 0
    alive = True
    
    while alive:
        dt = min(clock.tick(60) / 1000, 0.05)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                alive = False
    pygame.quit()

