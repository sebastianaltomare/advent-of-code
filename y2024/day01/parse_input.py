"""
Advent of Code 2024
Day 01
Sebastian Altomare

Parse Input
"""

def parse_input(file_name):
    """
    Reads input from a two-column text file and returns
    a column-based tuple of lists.
    
    Args:
        file_name (str): The name of the file to be read.
    
    Returns:
        Tuple(List[str], List[str]): A tuple containing a list of
            each column.
    """
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()
    list1, list2 = [], []
    for line in lines:
        a, b = map(int, line.split())
        list1.append(a)
        list2.append(b)
    return list1, list2
