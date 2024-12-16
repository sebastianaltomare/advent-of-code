"""
Advent of Code 2024
Day 03
Sebastian Altomare

Part Two
"""
import re
from parse_input import parse_input
from multiplier_sum import multiplier_sum

def conditional_add_sequences(file_name):
    """
    Compute the sum of the products of the mul(_,_) pairs in a file
    that come after do() and not after don't().
    
    Args:
        file_name (str): The name of the file to read.
        
    Returns:
        int: The sum of the products.
    """
    memory = parse_input(file_name)
    multipliers = parse_dos_and_donts(memory)
    return multiplier_sum(multipliers)

def parse_dos_and_donts(memory):
    """
    Helper function to parse which mul(_,_) structure come
    after do() and not after don't() in a string.
    
    Args:
        memory (str): The string to parse.
        
    Returns:
        List[Tuple(str, str)]: A list containing the appropriate
            mul(_,_) pairs.
    """
    expression = re.compile(r"mul\((\d+),(\d+)\)")
    do_segments = memory.split("do()")
    multipliers = []
    for do_segment in do_segments:
        if "don't()" in do_segment:
            do_segment = do_segment.split("don't()")[0]
        multipliers.extend(expression.findall(do_segment))
    return multipliers
