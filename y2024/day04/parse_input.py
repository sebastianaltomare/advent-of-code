"""
Advent of Code
Day 04
Sebastian Altomare

Parse Input
"""

def parse_input(file_name):
    """
    Reads a file containing a grid of letters and returns a dictionary
    mapping (x, y) grid coordinates to corresponding characters. 
    
    Args:
        file_name (str): The name or path of the file to be read.
        
    Returns:
        Dict[Tuple(int, int), str]: A dictionary where keys are (x, y) tuples 
        representing grid positions, and values are the corresponding letters.
    """
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.read().splitlines()
    except FileNotFoundError as error:
        raise FileNotFoundError(f"{file_name} not found.") from error

    return {
        (x, y): letter
        for y, line in enumerate(lines)
        for x, letter in enumerate(line)
    }
