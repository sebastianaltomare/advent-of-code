"""
Advent of Code 2024
Day 02
Sebastian Altomare

Part One
"""
from parse_input import parse_input
from safe import is_safe
from part_two import count_safe_helper

def count_safe(file_name):
    """
    Count the number of safe reports in a file.
    
    Args:
        file_name (str): The name of the file to be read.
        
    Returns:
        (int): the number of safe reports in a file.
    """
    puzzle = parse_input(file_name)
    return count_safe_helper(puzzle)