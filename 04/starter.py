# Game Designer · Lesson 04
# Read before running. Arrow keys move (lesson 2+); R resets (lesson 4+); Esc quits.
# studio.py handles the window and graphics; this file owns the game rules.
import studio as g

speed = 180

def reset():
    global x, y, score, collected, state
    x, y = 160, 300
    score = 0
    collected = False
    state = 'play'

reset()

def on_key(key):
    if key == 'r':
        reset()

def update(dt):
    global x, y, score, collected, state
    if state != 'play':
        return
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
    if not collected and g.touching(x, y, 560, 300):
        collected = True
        score += 10
        state = 'win'

def draw():
    g.background()
    g.picture('robot', x, y)
    if not collected:
        g.picture('battery', 560, 300)
    g.text('Score: ' + str(score) + ' | ' + state + ' | R resets', 24, 20)

if __name__ == '__main__':
    g.run(globals())
