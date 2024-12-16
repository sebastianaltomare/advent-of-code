"""
Advent of Code 2024
Day 01
Sebastian Altomare

Part One
"""

from parse_input import parse_input

def compute_total_distance(file_name):
    """
    Computes the distance between two lists and returns
    the result.
    
    Args:
        list1 (List[str]): The first list.
        list2 (List[str]): The second list.
    
    Returns:
        int: The distance between the two lists.
    """
    list1, list2 = parse_input(file_name)
    return sum(abs(a - b) for a, b in zip(sorted(list1), sorted(list2)))
