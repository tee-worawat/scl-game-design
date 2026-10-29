# Game Designer · Lesson 08
# Read before running. Arrow keys move (lesson 2+); R resets (lesson 4+); Esc quits.
# studio.py handles the window and graphics; this file owns the game rules.
import studio as g

speed = 180
# New idea: level data changes the challenge without changing collision rules.
levels = [
    {'targets': [(340, 180), (560, 400)], 'obstacles': [(400, 300)]},
    {'targets': [(340, 460), (600, 180)], 'obstacles': [(400, 300), (580, 360)]},
]

def load_level():
    global x, y, targets, obstacles
    x, y = 120, 300
    targets = levels[level]['targets'][:]
    obstacles = levels[level]['obstacles'][:]

def reset():
    global level, score, state
    level, score, state = 0, 0, 'play'
    load_level()

reset()

def on_key(key):
    if key == 'r':
        reset()

def update(dt):
    global x, y, score, state, level
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
    for target in targets[:]:
        if g.touching(x, y, target[0], target[1]):
            targets.remove(target)
            score += 10
    for obstacle in obstacles:
        if g.touching(x, y, obstacle[0], obstacle[1]):
            state = 'lose'
    if state == 'play' and len(targets) == 0 and g.touching(x, y, 720, 500):
        level += 1
        if level == len(levels):
            state = 'win'
        else:
            load_level()

def draw():
    g.background()
    g.picture('robot', x, y)
    for target in targets:
        g.picture('crystal', target[0], target[1])
    for obstacle in obstacles:
        g.picture('asteroid', obstacle[0], obstacle[1])
    g.picture('portal', 720, 500, 80)
    g.text('Stage ' + str(min(level+1, len(levels))) + ' | Score ' + str(score) + ' | ' + state, 24, 20)
    g.text('Collect every crystal, then enter the portal. R resets.', 24, 50, 20)

if __name__ == '__main__':
    g.run(globals())
