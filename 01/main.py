import pygame as g
g.init()
screen = g.display.set_mode((800, 600))
g.display.set_caption("Move your sprite!")
clock = g.time.Clock()

image_path = "01/images/robot.png"
player = g.image.load(image_path).convert_alpha()
player = g.transform.smoothscale(player, (64, 64))

running = True
while running:
    dt = clock.tick(60) / 1000

    for event in g.event.get():
        if event.type == g.QUIT:
            running == False

    if not running:
        break

    screen.fill("#FFFFFF")
    player_rect = player.get_rect(center=(round(200), round(200)))
    screen.blit(player, player_rect)
    g.display.flip()
g.quit()
