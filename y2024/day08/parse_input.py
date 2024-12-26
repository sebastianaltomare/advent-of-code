"""
Advent of Code 2024
Day 08
Sebastian Altomare

Parse Input
"""
from pathlib import Path

def parse_input(file_name):
    """
    Reads and parses a grid of characters from a text file into a
    coordinate-based dictionary representing a grid of frequency locations.
    
    Args:
        file_name (str): The name or path of the file to read.
        
    Returns:
        Dict[Tuple[int, int], str]: A dictionary mapping coordinates
            to a character.
    """
    path = Path(file_name)
    with path.open("r", encoding="utf-8") as file:
        lines = [line.rstrip() for line in file]

    return {
        (x, y): character
        for y, line in enumerate(lines)
        for x, character in enumerate(line)
    }
