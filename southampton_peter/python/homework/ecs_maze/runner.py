class Runner:

    def __init__(self, orientation, x=0, y=0):
        self.orientation = orientation
        self.x = x
        self.y = y


def create_runner(x: int = 0, y: int = 0, orientation: str = "N") -> Runner:
    return Runner(orientation, x, y)


def get_x(runner: Runner):
    return runner.x


def get_y(runner: Runner):
    return runner.y


def get_orientation(runner: Runner):
    return runner.orientation


def turn(runner: Runner, direction: str):
    orientations = ["N", "E", "S", "W"]
    idx = orientations.index(runner.orientation)
    if direction == "Right":
        result = (idx + 1) % 4
    elif direction == "Left":
        result = (idx - 1) % 4
    else:
        return runner
    runner.orientation = orientations[result]
    return runner


def forward(runner: Runner):
    if runner.orientation == "N":
        runner.y += 1
    elif runner.orientation == "E":
        runner.x += 1
    elif runner.orientation == "S":
        runner.y -= 1
    elif runner.orientation == "W":
        runner.x -= 1
    return runner
