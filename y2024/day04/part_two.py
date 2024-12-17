"""
Advent of Code 2024
Day 04
Sebastian Altomare

Part Two
"""
from parse_input import parse_input
from part_one import shift_loc, positioned

def x_mas_word_search(file_name):
    """
    Counts the number of 'X-MAS' occurences in a word search grid
    from a text file.
    
    Args:
        file_name (str): The name or path of the file to read.
        
    Returns:
        int: The total number of 'X-MAS' occurences.
    """
    grid = parse_input(file_name)
    return sum(1 for loc in grid if is_x_mas(grid, loc))

def is_x_mas(grid, loc):
    """
    Determine whether an 'X-MAS' occurence exists at a specified location.
    
    Args:
        grid (Dict[Tuple(int, int) : int]): The wordsearch grid.
        loc (Tuple(int, int)): The specified location.
        
    Returns:
        bool: True if an x-mas occurence is found, False otherwise.
    """
    return (
        diagonal(grid, shift_loc(loc, (-1, -1)), (1, 1)) and
        diagonal(grid, shift_loc(loc, (1, -1)), (-1, 1))
    )

def diagonal(grid, loc, route):
    """
    Determine whether the diagonals around a location correspond to
    an x-mas occurence.
    
    Args:
        grid (Dict[Tuple(int, int) : int]): The wordsearch grid.
        loc (Tuple(int, int)): The start of a diagonal.
        route (Tuple(int, int)): The direction in which to proceed.
        
    Returns:
        bool: True if a valid diagonal, False otherwise.
    """
    return (
        positioned(grid, loc, route, "MAS") or
        positioned(grid, loc, route, "MAS"[::-1])
    )
