"""Teacher reference: Robot Rescue. Standard-library Python; no graphics needed."""
def energy_after_move(energy, cost):
    """Return remaining energy; an unaffordable move leaves energy unchanged."""
    if cost < 0:
        raise ValueError('Cost must not be negative')
    if energy < cost:
        return energy
    return energy - cost


class Robot:
    def __init__(self, name, energy=3):
        self.name = name
        self.energy = energy
        self.position = 0

    def move(self):
        """Move one step for one energy. Return whether the move succeeded."""
        if self.energy < 1:
            return False
        self.energy = energy_after_move(self.energy, 1)
        self.position += 1
        return True

    def recharge(self):
        """A recharge turn adds two energy, up to a maximum of five."""
        self.energy = min(5, self.energy + 2)


def play():
    """Reach position four within six valid turns. Invalid commands cost no turn."""
    robot = Robot('Spark', 3)
    turns = 0
    print('ROBOT RESCUE | Reach the stranded explorer at position 4 in 6 turns.')
    while turns < 6 and robot.position < 4:
        print(f'Turn {turns + 1}/6 | position={robot.position} energy={robot.energy}')
        command = input('[m]ove [r]echarge [q]uit: ').strip().lower()
        if command == 'q':
            print('Mission paused. Run again for a fresh robot.')
            return
        if command not in ('m', 'r'):
            print('Choose m, r, or q. No turn spent.')
            continue
        turns += 1
        if command == 'm':
            if not robot.move():
                print('No energy: the turn is spent. Recharge next time.')
        else:
            robot.recharge()
    print('Rescue complete!' if robot.position >= 4 else 'Out of turns. Try a new plan.')


if __name__ == '__main__':
    play()
