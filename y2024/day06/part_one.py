"""
Advent of Code 2024
Day 06
Sebastian Altomare

Part One
"""
from parse_input import parse_input

DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]
OBSTACLE = "#"
VISITED = "X"
OPEN = "."

def compute_number_of_visited(file_name):
    """
    Computes the number of locations visited by the guard.

    Args:
        file_name (str): The name or path of the file to read.

    Returns:
        int: The number of locations visited.
    """
    grid, starting_position = parse_input(file_name)
    visited = simulate_movement(grid, starting_position, (0, -1))
    return len(visited)


def simulate_movement(grid, starting_position, direction):
    """
    Simulates the guard's movement through the grid and tracks
    visited locations.
    
    Args:
        grid (Dict[Tuple[int, int] : str]): A grid representing obstacles
            and the guard's movement.
        starting_position (Tuple(int, int)): The starting position of the guard.
        direction (Tuple(int, int)): The initial direction of the 
            guard's movement.
    
    Returns:
        set: A set of all locations visited by the guard.
    """
    visited = set()

    while True:
        visited.add(starting_position)
        x, y = starting_position
        dx, dy = direction
        new_position = (x + dx, y + dy)

        if new_position not in grid:
            break

        if grid[new_position] == OBSTACLE:
            index = DIRECTIONS.index(direction)
            direction = DIRECTIONS[index - 3]
            continue
        starting_position = new_position
    return visited
