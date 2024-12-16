"""
Advent of Code 2024
Day 02
Sebastian Altomare

Safe
"""

def is_safe(rep):
    """
    Checks if a level is safe.
    
    Args:
        rep (List[int]): a list of integers representing a level.
        
    Returns:
        (bool): True if safe, False otherwise.
    """
    pos, neg = {1, 2, 3}, {-1, -2, -3}
    differences = {rep[i + 1] - rep[i] for i in range(len(rep) - 1)}
    return differences <= pos or differences <= neg

def is_dampened_safe(rep):
    """
    Checks if a level is safe with one element removed.
    
    Args:
        rep (List[int]): a list of integers representing a level.
    
    Returns:
        (bool): True if safe, False otherwise.
    """
    return any(is_safe(rep[:i] + rep[i+1:]) for i, _ in enumerate(rep))
