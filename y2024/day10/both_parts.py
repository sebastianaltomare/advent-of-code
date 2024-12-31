"""
Advent of Code 2024
Day 10
Sebastian Altomare

Both Parts
"""
from collections import deque
from parse_input import parse_input

def trailhead_computation(file_name, distinct=True):
    """
    Computes the sum of all trailhead scores or ratings.
    
    Args:
        file_name (str): The name or path of the input file.

    Returns:
        int: The sum of all scores or ratings.
    """
    grid = parse_input(file_name)
    score = 0

    for location, height in grid.items():
        if height == 0:
            if distinct:
                score += count_peaks(grid, location)
            else:
                score += count_paths(grid, location)
    return score


def count_peaks(grid, location):
    """
    Counts distinct peaks from a given trailhead.
    
    Args:
        grid (Dict[Tuple[int, int], int]): The topographic map as a dictionary.
        location (Tuple[int, int]): The starting location of the trailhead.
        
    Returns:
        int: The number of distinct peaks.
    """
    queue = deque([(location, 0)])
    visited = set()
    counter = 0

    while queue:
        loc, height = queue.popleft()
        for neighbor in get_adjacent_locations(loc):
            if invalid_next_step(grid, neighbor, height, visited):
                continue
            visited.add(neighbor)
            if grid[neighbor] == 9:
                counter += 1
            else:
                queue.append((neighbor, height + 1))
    return counter


def count_paths(grid, location):
    """
    Counts distinct valid trails from a given starting location.
    
    Args:
        grid (Dict[Tuple[int, int], int]): The topographic map as a dictionary.
        location (Tuple[int, int]): The starting location of the trailhead.
    
    Returns:
        int: The numebr of distinct valid trails.
    """
    queue = deque([(location, 0, [])])
    counter = 0

    while queue:
        loc, height, path = queue.popleft()
        for neighbor in get_adjacent_locations(loc):
            if invalid_next_step(grid, neighbor, height, path):
                continue
            if grid[neighbor] == 9:
                counter += 1
            else:
                queue.append((neighbor, height + 1, path + [neighbor]))
    return counter


def invalid_next_step(grid, location, height, container):
    """
    Determine if the next possible step on a hiking trail is valid.
    
    Args:
        grid (Dict[Tuple[int, int], int]): The topographic map as a dictionary.
        location (Tuple[int, int]): The starting location of the trailhead.
        height (int): The current topographic height of the trail.
        container (List | Set): Structure containing past steps on the trail.
    
    Returns:
        bool: True if the next step is valid, False otherwise.
    """
    return location in container or grid.get(location) != height + 1


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
