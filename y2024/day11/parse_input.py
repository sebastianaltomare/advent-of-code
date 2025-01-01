""""
Advent of Code 2024
Day 11
Sebastian Altomare

Parse Input
"""
from collections import Counter

def parse_input(file_name):
    """
    Parses input from a text file into a Counter object.

    Args:
        file_name (str): Path to the input file.

    Returns:
        Counter[int]: A Counter object mapping integers to their counts.
    """
    with open(file_name, "r", encoding="utf-8") as file:
        return Counter(map(int, file.read().split()))
