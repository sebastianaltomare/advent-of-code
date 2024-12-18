"""
Advent of Code
Day 05
Sebastian Altomare

Part One
"""
from parse_input import parse_input

def sum_correct_order_middle_page_numbers(file_name):
    """
    Compute the sum of the middle page numbers of correctly
    ordered updates.
    
    Args:
        file_name (str): The name or path of the input file.
        
    Returns:
        int: The sum of the middle page numbers.
    """
    rule_graph, updates = parse_input(file_name)
    return sum(
        find_middle_page_number(update)
        for update in updates
        if is_in_correct_order(rule_graph, update)
    )

def is_in_correct_order(rule_graph, update):
    """
    Checks if an update is correctly ordered based on the given rules.
    
    Args:
        rule_graph (Dict[int, Set[int]]): A dictionary storing ordering rules.
        update (List[int]): The update to check.
        
    Returns:
        bool: True if correctly ordered, False otherwise.
    """
    length = len(update) - 1
    return all(update[i + 1] in rule_graph[update[i]] for i in range(length))

def find_middle_page_number(update):
    """
    Finds the middle page number of an update.
    
    Args:
        update (List[int]): The update.
    
    Returns:
        int: The middle page number
    """
    assert len(update) % 2 == 1
    return update[len(update) // 2]
