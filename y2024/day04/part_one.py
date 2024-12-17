"""
Advent of Code
Day 04
Sebastian Altomare

Part One
"""
from parse_input import parse_input

routes = [(0, -1), (1, -1), (1, 0), (1, 1),
              (0, 1), (-1, 1), (-1, 0), (-1, -1)]

def xmas_word_search(file_name):
    """
    Counts the number of occurences of the word 'XMAS' in a word search grid 
    from a text file.
    
    Args:
        file_name (str): The name or path of the file to read.
        
    Returns:
        int: The total number of 'XMAS' occurences.
    """
    grid = parse_input(file_name)
    return sum(count_xmas(grid, loc, "XMAS") for loc in grid)

def count_xmas(grid, loc, aim):
    """
    Count the occurences of 'XMAS' from a specific grid location.
    
    Args:
        grid (Dict[Tuple(int, int) : int]): The wordsearch grid.
        loc (Tuple(int, int)): The location to check for xmas occurences.
        aim (str): The string to be found.
    
    Returns:
        int: The number of 'XMAS' at the given location.
    """
    return sum(positioned(grid, loc, route, aim) for route in routes)

def positioned(grid, loc, route, aim):
    """
    Determine whether starting a location and proceeding in a
    certain direction will yield in an xmas occurence.
    
    Args:
        grid (Dict[Tuple(int, int) : int]): The wordsearch grid.
        loc (Tuple(int, int)): The location to check for xmas occurences.
        route (Tuple(int, int)): The direction to proceed.
        aim (str): The string to be found.
        
    Returns:
        bool: True if an xmas occurence is found, False otherwise.
    """
    if not aim:
        return True
    return grid.get(loc, "") == aim[0] and positioned(
        grid, shift_loc(loc, route), route, aim[1:]
    )

def shift_loc(loc, shift):
    """
    Computes the new location after a specified shift.
    
    Args:
        loc (Tuple(int, int)): The starting location.
        shift (Tuple(int, int)): The shift to be executed.
        
    Returns:
        Tuple(int, int): The new location after the specified shift.
    """
    x, y,= loc
    shift_x, shift_y = shift
    return (x + shift_x, y + shift_y)
