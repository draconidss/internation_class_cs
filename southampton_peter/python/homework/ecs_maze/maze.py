def create_maze(width=5, height=5):
    maze = []
    for _ in range(height):
        maze.append([dict(s=False, n=False, e=False, w=False) for _ in range(width)])

    return maze


maze_create = create_maze(11, 5)
for row in maze_create:
    print(row)

# x = 2, h = 4
def add_horizontal_wall(maze, x_coordinate, horizontal_line):
    maze[horizontal_line][x_coordinate]["s"] = True
    maze[horizontal_line - 1][x_coordinate]["s"] = True

    return maze


def add_vertical_wall(maze, y_coordinate, vertical_line):
    maze[y_coordinate][vertical_line] = "vline"
    return maze


def get_dimensions(maze) -> tuple[int, int]:
    return (len(maze[0]), len(maze))


def get_walls(
    maze, x_coordinate: int, y_coordinate: int
) -> tuple[bool, bool, bool, bool]:
    w, n, e, s = False, False, False, False
    
    if maze[y_coordinate][x_coordinate] == :
        s = True

    elif maze[y_coordinate][x_coordinate] == "vline":
    else:

