"""
Advent of Code 2024
Day 03
Sebastian Altomare

Multiplier Sum
"""

def multiplier_sum(multipliers):
    """
    Helper function to computes the sum of the products of 
    the pairs inside each mul(_,_) structure.
    
    Args:
        multipliers (List[Tuple(str, str)]): A list of tuples 
            that represent the pairs inside each mul(_,_) structure.
    
    Returns:
        int: The sum of the products of the integer pairs.
    """
    try:
        return sum(int(first) * int(second) for first, second in multipliers)
    except ValueError as error:
        raise ValueError("Not all elements are valid integers") from error
