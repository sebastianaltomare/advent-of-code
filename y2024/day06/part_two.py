"""
Advent of Code 2024
Day 06
Sebastian Altomare

Part Two
"""
from parse_input import parse_input
from part_one import simulate_movement

DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]
OBSTACLE = "#"
VISITED = "X"
OPEN = "."

def count_obstruction_positions(file_name):
    """
    Count the number of positions that cause the guard to enter a loop
    if an obstacle is placed there.
    
    Args:
        file_name (str): The name or path of the file to read.
        
    Returns:
        int: The number of obstruction positions.
    """
    grid, starting_position = parse_input(file_name)
    visited = simulate_movement(grid, starting_position, (0, -1))

    obstructions = 0
    for visited_position in visited:
        grid[visited_position] = OBSTACLE
        obstructions += is_loop(grid, starting_position, (0, -1))
        grid[visited_position] = OPEN
    return obstructions

def is_loop(grid, starting_position, direction):
    """
    Determine if the guard will enter a loop in the given grid.
    
    Args:
        grid (Dict[Tuple(int, int) : str]): A grid representing the 
            obstacles and the guard's movement.
        starting_position (Tuple(int, int)): The starting position of the guard.
        direction (Tuple(int, int)): The direction of the guard's movement.
    
    Returns:
        int: 1 if loop, 0 otherwise.
    """
    visited = set([(starting_position, direction)])

    while True:
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

        if (starting_position, direction) in visited:
            return 1

        visited.add((starting_position, direction))
    return 0
