"""
Advent of Code 2024
Day 03
Sebastian Altomare

Part One
"""
import re
from parse_input import parse_input
from multiplier_sum import multiplier_sum

def add_sequences(file_name):
    """
    Compute the sum of the products of the mul(_,_) pairs in a file.
    
    Args:
        file_name (str): The name of the file to read.
        
    Returns:
        int: The sum of the products.
    """
    memory = parse_input(file_name)
    expression = r"mul\((\d+),(\d+)\)"
    multipliers = re.findall(expression, memory)
    return multiplier_sum(multipliers)
