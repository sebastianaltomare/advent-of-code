"""
Advent of Code 2024
Day 05
Sebastian Altomare

Parse Input
"""
from collections import defaultdict

def parse_input(file_name):
    """
    Reads a file containing ordering rules and updates.
    
    Args:
        file_name (str): The name or path of the file to be read.
        
    Returns:
        Tuple(Dict(int, Set[int]), List[List[int]]): A tuple containing
        a dictionary representing the ordering rules and a list of updates
        as lists of page numbers.
    """
    with open(file_name, "r", encoding="utf-8") as file:
        rules, updates = file.read().split("\n\n")

    rule_graph = defaultdict(set)
    for line in rules.splitlines():
        first, following = map(int, line.split("|"))
        rule_graph[first].add(following)

    updates = [list(map(int, line.split(","))) for line in updates.splitlines()]
    return rule_graph, updates
