"""
Advent of Code 2024
Day 08
Sebastian Altomare

Both Parts
"""
from parse_input import parse_input
NOTHING = "."

def total_antinode_locations(file_name, res=False):
    """
    Compute the number of distinct antinode locations, for both 
    resonance and non-resonance systems.
    
    Args:
        file_name (str): The name of path of the file to read.
        res (bool): True if a resonant system, False otherwise. Default False.
    
    Returns:
        int: The number of distinct antinode locations.
    """
    grid = parse_input(file_name)
    rows, columns = max(grid.keys())
    loc_set = set()
    for (x, y), frequency_type in grid.items():
        if frequency_type == NOTHING:
            continue

        for j in range(y + 1, columns + 1):
            for i in range(rows + 1):
                if grid.get((i, j)) != frequency_type:
                    continue

                if (x, y) != (i, j):
                    process_antinodes(grid, (x, y), (i, j), loc_set, res)
    return len(loc_set)


def process_antinodes(grid, loc, found, loc_set, res):
    """
    Update a given set with distinct antinode locations:
    
    Args:
        grid (Dict[Tuple[int, int], str]): A grid representing the frequency 
            locations on a grid.
        loc (Tuple[int, int]): The location of one frequency location.
        found (Tuple[int, int]): The location of another same-frequency 
            location.
        loc_set (Set[Tuple[int, int]]): A set containing the distinct 
            antinode locations on the grid.
        res (bool): True if a resonant system, False otherwise. Default False.
    
    Returns:
        None: Updates the set in place.
    """
    x, y, i, j = unpack_location_and_found(loc, found)
    dx = i - x
    dy = j - y
    add_antinodes(grid, get_antinodes(grid, loc, found, (dx, dy), res), loc_set)


def add_antinodes(grid, antinodes, antinode_set):
    """
    Add given antinodes to the antinode set if they lie on the grid.
    
    Args:
        grid (Dict[Tuple[int, int], str]): A grid representing the frequency 
            locations on a grid.
        antinodes (List[Tuple[int, int]]): A list containing possible antinodes.
        antinode_set (Set[Tuple[int, int]]): A set containing the distinct 
            antinode locations on the grid.

    Returns:
        None: Updates the set in place.
    """
    for antinode in antinodes:
        if antinode in grid:
            antinode_set.add(antinode)


def get_antinodes(grid, loc, found, change, res):
    """
    Get the antinodes of a frequency location pair.
    
    Args:
        grid (Dict[Tuple[int, int], str]): A grid representing the frequency 
            locations on a grid.
        loc (Tuple[int, int]): The location of one frequency location.
        found (Tuple[int, int]): The location of another same-frequency 
            location.
        dx (int): The row change between the two frequency locations.
        dy (int): The column change between the two frequency locations.
        res (bool): True if a resonant system, False otherwise. Default False.

    Returns:
        List[Tuple[int, int]]: A list contaning the corresponding antinodes.
    """
    x, y, i, j = unpack_location_and_found(loc, found)
    dx, dy = change
    if res:
        return find_resonant_antinodes(grid, (x, y), dx, dy)
    return [(x - dx, y - dy), (i + dx, j + dy)]


def find_resonant_antinodes(grid, loc, dx, dy, increment=0):
    """
    Get the antinodes for a resonant system.

    Args:
        grid (Dict[Tuple[int, int], str]): A grid representing the frequency 
            locations on a grid.
        loc (Tuple[int, int]): The location of one frequency location.
        dx (int): The row change between the two frequency locations.
        dy (int): The column change between the two frequency locations.
        increment (int): Counter to track the distance of each
            succesive antinode. Default 0.
    """
    antinodes = []
    x, y = loc
    while True:
        antinode1 = (x - increment * dx, y - increment * dy)
        antinode2 = (x + increment * dx, y + increment * dy)
        if antinode1 not in grid and antinode2 not in grid:
            increment = 0
            break
        antinodes.extend([antinode1, antinode2])
        increment += 1
    return antinodes


def unpack_location_and_found(location, found):
    """
    Unpack the row and column coordinates a frequency location pair.
    
    Args:
        loc (Tuple[int, int]): The location of one frequency location.
        found (Tuple[int, int]): The location of another same-frequency 
            location.

    Returns:
        Tuple[int, int, int, int]: A tuple containing each coordinate.
    """
    x, y = location
    i, j = found
    return x, y, i, j
