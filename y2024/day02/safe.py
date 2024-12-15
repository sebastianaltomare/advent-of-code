"""
Advent of Code 2024
Day 02
Sebastian Altomare

Safe
"""

def is_level_ordered(rep):
    """
    Checks if a level is ordered.
    
    Args:
        rep (List[int]): a list of integers representing a level.
        
    Returns:
        (bool): True if ordered, False otherwise.
    """
    return (
        len(set(rep)) == len(rep) and
        rep == sorted(rep) or rep == sorted(rep, reverse=True)
    )

def correct_range(rep):
    """
    Checks if a level has correct ranges.
    
    Args:
        rep (List[int]): a list of integers representing a level.
        
    Returns:
        (bool): True if has correct ranges, False otherwise.
    """
    return all(1 <= abs(rep[i] - rep[i + 1]) <= 3 for i in range(len(rep) - 1))

def is_safe(rep):
    """
    Checks if a level is safe.
    
    Args:
        rep (List[int]): a list of integers representing a level.
        
    Returns:
        (bool): True if safe, False otherwise.
    """
    return is_level_ordered(rep) and correct_range(rep)
