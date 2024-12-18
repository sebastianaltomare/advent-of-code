"""
Advent of Code
Day 05
Sebastian Altomare

Part Two
"""
from functools import cmp_to_key
from parse_input import parse_input
from part_one import is_in_correct_order, find_middle_page_number

def sum_incorrect_order_middle_page_numbers(file_name):
    """
    Compute the sum of the middle page numbers of reordered incorrectly
    ordered updates.
    
    Args:
        file_name (str): The name or path to the input file.
        
    Returns:
        int: The sum of the middle page numbers after reordering 
            incorrectly ordered updates.
    """
    rule_graph, updates = parse_input(file_name)
    return sum(
        find_middle_page_number(reorder(rule_graph, update))
        for update in updates
        if not is_in_correct_order(rule_graph, update)
    )

def reorder(rule_graph, update):
    """
    Reorders an incorrectly ordered update based on the given rules.
    
    Args:
        rule_graph (Dict[int, Set[int]]): A dictionary storing ordering rules.
        update (List[int]): The update to reorder.
    
    Returns:
        List[int]: The reordered update.
    """
    def compare(a, b):
        if b in rule_graph[a]:
            return -1
        return 1
    return sorted(update, key=cmp_to_key(compare))
