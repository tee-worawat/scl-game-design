# Game Designer · Lesson 01
# Read before running. Arrow keys move (lesson 2+); R resets (lesson 4+); Esc quits.
# studio.py handles the window and graphics; this file owns the game rules.
import studio as g

x = 160
y = 300

def draw():
    g.background()
    g.picture('robot', x, y)
    g.text('Mission 1: place your robot', 24, 20)

if __name__ == '__main__':
    g.run(globals())
