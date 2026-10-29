# Game Designer · Lesson 02
# Read before running. Arrow keys move (lesson 2+); R resets (lesson 4+); Esc quits.
# studio.py handles the window and graphics; this file owns the game rules.
import studio as g

x, y = 160, 300
speed = 180

def update(dt):
    global x, y
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

def draw():
    g.background()
    g.picture('robot', x, y)
    g.picture('landing_pad', 640, 300, 96)
    g.text('Reach the landing pad. Arrow keys move.', 24, 20)

if __name__ == '__main__':
    g.run(globals())
