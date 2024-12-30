"""
Advent of Code 2024
Day 09
Sebastian Altomare

Part One
"""
from parse_input import parse_input
FREE = "."

def checksum(file_name):
    """
    Computes the checksum of a file system with fragmentation.
    
    Args:
        file_name (str): The path or name of the file to read.
    
    Returns:
        int: The checksum of the file system.
    """
    blocks = parse_input(file_name)
    i = 0
    while i < len(blocks):
        if blocks[i] == FREE:
            if not blocks:
                break
            blocks[i] = blocks.pop()
        i += 1
    return sum(i * val for i, val in enumerate(blocks))
