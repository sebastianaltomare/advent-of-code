"""
Advent of Code 2024
Day 02
Sebastian Altomare

Parse Input
"""

def parse_input(file_name):
    """
    Reads and checks input from a text file and returns
    a list of lists of integers.

    Args:
        file_name (str): The name of the file to be read.

    Returns:
        (List[List[int]]): A list containing lists of integers.
    """
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return [parse_report(rep) for rep in file]
    except FileNotFoundError:
        raise FileNotFoundError(f"{file_name} not found.")
    except ValueError as error:
        raise ValueError(f"Error parsing {error}")
    
def parse_report(rep):
    """
    Converts a string of integer values into a list of integers.
    
    Args:
        rep (str): A string containing integer values.
        
    Returns:
        (List[int]): A list of integers.
    """
    return [int(value) for value in rep.split()]
