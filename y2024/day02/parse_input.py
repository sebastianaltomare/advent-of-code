"""
Advent of Code 2024
Day 02
Sebastian Altomare

Parse Input
"""

def parse_input(file_name):
    """
    Reads a text file and parses its content into a list
    of integer lists.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        List[List[int]]: A list of integer lists.
    """
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return [parse_report(line) for line in file if line.strip()]
    except FileNotFoundError:
        raise FileNotFoundError(f"File {file_name} not found.")
    except ValueError as error:
        raise ValueError(f"Error parsing {error}")
    
def parse_report(line):
    """
    Converts a string of integer values into a list of integers.
    
    Args:
        rep (str): A string containing integer values.
        
    Returns:
        List[int]: A list of integers.
    """
    try:
        return [int(value) for value in line.split()]
    except ValueError:
        raise ValueError(f"Invalid data")
