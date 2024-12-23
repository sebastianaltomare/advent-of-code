"""
Advent of Code
Day 07
Sebastian Altomare

Both Parts
"""
from itertools import product
from parse_input import parse_input

def total_calibration_result(file_name, concatenation=False):
    """
    Compute the total calibration result of the data.
    
    Args:
        file_name (str): The name or path of the file to read.
        concatenation (bool): True if including the concatenate operator,
            False otherwise.
            
    Returns:
        int: The sum of all calibrated values.
    """
    calibrations = parse_input(file_name)
    return sum(target
               for target, numbers in calibrations
               if are_equal(target, numbers, concatenation))


def are_equal(target, numbers, concatenation):
    """
    Determine if the numbers can be manipulated using the available operators
    to equal the target value.
    
    Args:
        target (int): The target value of the arithmetic.
        numbers (List[int]): A list of the numbers used in the arithmetic.
        concatenation (bool): True if including the concatenate operator,
            False otherwise.

    Returns:
        bool: True if target value achieved, False otherwise.
    """
    operations = ["*", "+"]
    if concatenation:
        operations.append("||")
    operator_orders = product(operations, repeat=len(numbers) - 1)
    for operators in operator_orders:
        if target == evaluate(numbers, operators):
            return True
    return False


def evaluate(numbers, operators):
    """
    Evaluate the arithmetic of the numbers based on the given order
    of the operators.
    
    Args:
        numbers (List[int]): A list of the numbers used in the arithmetic.
        operators (List[str]): A list of the operators in the usage order.

    Returns:
        int: The value achieved by performing the arithmetic.
    """
    running_value = numbers[0]
    for i, operator in enumerate(operators):
        if operator == "+":
            running_value += numbers[i + 1]
        elif operator == "*":
            running_value *= numbers[i + 1]
        elif operator == "||":
            running_value = int(f"{running_value}{numbers[i + 1]}")
    return running_value
