"""
Advent of Code 2024
Day 10
Sebastian Altomare

Parse Input
"""
from pathlib import Path

def parse_input(file_name):
    """
    Parses the input file into a dictionary mapping grid positions to
    topographic heights.
    
    Args:
        file_name (str): The name or path of the input file.
        
    Returns:
        Dict[Tuple[int, int] int]: A grid whose keys are (x,y) positions and
            whose values are the corresponding topographic height.
    """
    with Path(file_name).open("r", encoding="utf-8") as file:
        return {
            (x, y): int(height)
            for y, line in enumerate(file)
            for x, height in enumerate(line.strip())
        }