# Game Designer · Lesson 06
# Read before running. Arrow keys move (lesson 2+); R resets (lesson 4+); Esc quits.
# studio.py handles the window and graphics; this file owns the game rules.
import studio as g

speed = 180

def reset():
    global x, y, score, targets, obstacles, state
    x, y = 120, 300
    score = 0
    targets = [(360, 180), (540, 300), (360, 460)]
    obstacles = [(360, 300), (620, 440)]
    state = 'play'

reset()

def on_key(key):
    if key == 'r':
        reset()

def update(dt):
    global x, y, score, state
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
    # A copy lets us remove a collected target without skipping the next one.
    for target in targets[:]:
        if g.touching(x, y, target[0], target[1]):
            targets.remove(target)
            score += 10
    for obstacle in obstacles:
        if g.touching(x, y, obstacle[0], obstacle[1]):
            state = 'lose'
    if len(targets) == 0 and state == 'play':
        state = 'win'

def draw():
    g.background()
    g.picture('robot', x, y)
    for target in targets:
        g.picture('crystal', target[0], target[1])
    for obstacle in obstacles:
        g.picture('asteroid', obstacle[0], obstacle[1])
    g.text('Score: ' + str(score) + ' | ' + state + ' | R resets', 24, 20)

if __name__ == '__main__':
    g.run(globals())
