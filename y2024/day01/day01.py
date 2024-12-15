"""
Advent of Code 2024
Day 01
Sebastian Altomare
"""
from collections import Counter

def read_input(file_name):
    """
    Reads input from a two-column text file and returns
    a column-based tuple of lists.
    
    Args:
        file_name (str): The name of the file to be read.
    
    Returns:
        ((List[str], List[str])): A tuple containing a list of
            each column.
    """
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()
    list1, list2 = [], []
    for line in lines:
        first, second = line.split()
        list1.append(int(first))
        list2.append(int(second))
    return list1, list2

def compute_total_distance(file_name):
    """
    Computes the distance between two lists and returns
    the result.
    
    Args:
        list1 (List[str]): The first list.
        list2 (List[str]): The second list.
    
    Returns:
        (int): The distance between the two lists.
    """
    list1, list2 = read_input(file_name)
    list1.sort()
    list2.sort()
    return sum(abs(value - list2[i]) for i, value in enumerate(list1))

def compute_similarity_score(file_name):
    """
    Computes the similarity between two lists and returns
    the result.
    
    Args:
        list1 (List[str]): The first list.
        list2 (List[str]): The second list.
    
    Returns:
        (int): The similarity of two lists.
    """
    list1, list2 = read_input(file_name)
    multiplicity_map = Counter(list2)
    return sum(value * multiplicity_map[value] for value in list1)
