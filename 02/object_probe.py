# Predict before running. None means no image is needed for this position-only trace.
from main import Player

nova = Player(160, 300, None)
pip = Player(500, 300, None)
nova.move(1, 0, 0.05)
print(nova.x, pip.x)
