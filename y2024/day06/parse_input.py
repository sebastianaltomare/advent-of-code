"""
Advent of Code 2024
Day 06
Sebastian Altomare

Parse Input
"""
VISITED = "X"

def parse_input(file_name):
    """
    Reads a file containing a grid of obstacles and the position of a guard.
    
    Args:
        file_name (str): The name or path of the file to read.
        
    Returns:
        Tuple[Dict[Tuple(int, int) : str], Tuple[int, int]]: A tuple
            containing the grid detailed by the file and the starting 
            position of the guard.
    """
    with open(file_name, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file]

    grid = {}
    starting_position = None
    for y, line in enumerate(lines):
        for x, element in enumerate(line):
            if element == "^":
                starting_position = (x, y)
                grid[(x, y)] = VISITED
                continue
            grid[(x, y)] = element
    return grid, starting_position
