"""
Advent of Code 2024
Day 02
Sebastian Altomare

Part Two
"""
from parse_input import parse_input
from safe import is_dampened_safe

def count_dampened_safe(file_name):
    """
    Count the number of dampened safe reports in a file.
    
    Args:
        file_name (str): The name of the file to be read.
        
    Returns:
        (int): the number of dampened safe reports in a file.
    """
    puzzle = parse_input(file_name)
    return sum(is_dampened_safe(report) for report in puzzle)
