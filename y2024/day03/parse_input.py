"""
Advent of Code 2024
Day 03
Sebastian Altomare

Parse Input
"""

def parse_input(file_name):
    """
    Reads and returns the content of a text file as a string.
    
    Args:
        file_name (str): The name or path of the file to be read.
        
    Returns:
        str: The content of the file.
    """
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError as error:
        raise FileNotFoundError(f"{file_name} not found.") from error
