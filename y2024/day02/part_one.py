"""
Advent of Code 2024
Day 02
Sebastian Altomare

Part One
"""
from parse_input import parse_input
from safe import is_safe

def count_safe(file_name):
    """
    Count the number of safe reports in a file.
    
    Args:
        file_name (str): The name or path of the file to be read.
        
    Returns:
        int: The number of safe reports in a file.
    """
    puzzle = parse_input(file_name)
    return sum(is_safe(report) for report in puzzle)
