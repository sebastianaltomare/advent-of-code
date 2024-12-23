"""
Advent of Code
Day 07
Sebastian Altomare

Parse Input
"""

def parse_input(file_name):
    """
    Reads a file containing lines of calibration and returns the target
    and the number used in a list of tuples.
    
    Args:
        file_name (str): The name or path of the file to read.
        
    Returns:
        List[Tuple[int, List[int]]]: A list of tuples containing the 
            target value and the numbers used.
    """
    with open(file_name, "r", encoding="utf-8") as file:
        data = list(map(str.strip, file.readlines()))

    return [(int(target), list(map(int, numbers.split())))
            for line in data
            for target, numbers in [line.split(":")]]
