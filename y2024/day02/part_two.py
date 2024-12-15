"""
Advent of Code 2024
Day 02
Sebastian Altomare

Part Two
"""

from parse_input import parse_input
from safe import is_safe

def count_safe_helper(puzzle):
    """
    Count the number of safe reports in a file.
    
    Args:
        file_name (str): The name of the file to be read.
        
    Returns:
        (int): The number of safe reports in a file.
    """
    return [is_safe(rep) for rep in puzzle].count(True)

def count_dampener_results(file_name):
    """
    Count the number of safe reports in a dampened file.
    
    Args:
        file_name (str): The name of the file to be read.
        
    Returns:
        (int): The number of safe reports in the dampened file.
    """
    puzzle = parse_input(file_name)
    dampened_puzzle = []
    for rep in puzzle:
        if is_safe(rep):
            dampened_puzzle.append(rep)
        else:
            for i, _ in enumerate(rep):
                modified_level = rep[:i] + rep[i + 1:]
                if is_safe(modified_level):
                    dampened_puzzle.append(modified_level)
                    break
    return count_safe_helper(dampened_puzzle)
