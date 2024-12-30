"""
Advent of Code 2024
Day 10
Sebastian Altomare

Part One
"""
from parse_input import parse_input

def sum_trailhead_scores(file_name):
    """
    Computes the sum of all trailhead scores.
    
    Args:
        file_name (str): The name or path of the input file.

    Returns:
        int: The sum of all scores.
    """
    grid = parse_input(file_name)
    score = 0
    for location, height in grid.items():
        if height == 0:
            visited_peaks = set()
            trailhead_paths(grid, location, visited_peaks, height=0)
            score += len(visited_peaks)
    return score


def trailhead_paths(grid, location, visited_peaks, height=0):
    """
    Recursively adds reachable peak positions from the given trailhead to a set.
    
    Args:
        grid (Dict[Tuple[int, int], int]): The topographic map.
        location (Tuple[int, int]): The current location on the map.
        visited_peaks (Set[Tuple[int, int]]): The set of reachable peaks.
        height (int): The topographic height of the given location.
    
    Returns:
        None: Updates the set in place.
    """
    for next_location in get_adjacent_locations(location):
        if is_trail_sequential(grid, next_location, height):
            if grid[next_location] == 9:
                visited_peaks.add(next_location)
            else:
                trailhead_paths(grid, next_location, visited_peaks, height + 1)
            

def get_adjacent_locations(location):
    """
    Returns the adjacent positions to the given location.
    
    Args:
        location (Tuple[int, int]): The current location on the map.
    
    Returns:
        List[Tuple[int, int]]: A list of the adjacent locations.
    """
    x, y = location
    return [
        (x - 1, y),
        (x, y - 1),
        (x + 1, y),
        (x, y + 1)
    ]


def is_trail_sequential(grid, location, height):
    """
    Determines whether the next location on the trail is valid.
    
    Args:
        grid (Dict[Tuple[int, int], int]): The topographic map.
        location (Tuple[int, int]): The current location on the map.
        height (int): The topographic height of the given location.
    
    Returns:
        bool: True if sequential step, False otherwise.
    """
    return grid.get(location) == height + 1