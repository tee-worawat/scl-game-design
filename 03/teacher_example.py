# Game Designer · Lesson 03
# Read before running. Arrow keys move (lesson 2+); R resets (lesson 4+); Esc quits.
# studio.py handles the window and graphics; this file owns the game rules.
import studio as g

x, y = 160, 300
speed = 180
collected = False

def update(dt):
    global x, y, collected
    if g.held('left'):
        x -= speed * dt
    if g.held('right'):
        x += speed * dt
    if g.held('up'):
        y -= speed * dt
    if g.held('down'):
        y += speed * dt
    x = max(32, min(768, x))
    y = max(110, min(568, y))
    if not collected and g.touching(x, y, 560, 440):
        collected = True

def draw():
    g.background()
    g.picture('robot', x, y)
    if not collected:
        g.picture('crystal', 560, 440)
    g.text('Collected: ' + str(collected), 24, 20)

if __name__ == '__main__':
    g.run(globals())
