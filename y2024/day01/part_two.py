"""
Advent of Code 2024
Day 01
Sebastian Altomare

Part Two
"""

import parse_input
from collections import Counter

def compute_similarity_score(file_name):
    """
    Computes the similarity between two lists and returns
    the result.
    
    Args:
        list1 (List[str]): The first list.
        list2 (List[str]): The second list.
    
    Returns:
        (int): The similarity of two lists.
    """
    list1, list2 = parse_input(file_name)
    multiplicity_map = Counter(list2)
    return sum(value * multiplicity_map.get(value, 0) for value in list1)
