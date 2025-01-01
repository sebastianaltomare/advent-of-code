"""
Advent of Code 2024
Day 11
Sebastian Altomare

Both Parts
"""
from collections import Counter
from parse_input import parse_input

def blink(file_name, blinks):
    """
    Computes the total number of stones after a given number of blinks.
    
    Args:
        file_name (str): Path to the input file.
        blinks (int): The number of blinks to process.
    
    Returns:
        int: The total number of stones after blinks.
    """
    stones = parse_input(file_name)
    for _ in range(blinks):
        stones = blink_rearrange(stones)
    return sum(stones.values())


def blink_rearrange(stones):
    """
    Process one blink and updates the stone counts.

    Args:
        stones (Counter[int]): A Counter object mapping stone to their counts.

    Returns:
        Counter[int]: Updated Counter object mapping stones to their new counts.
    """
    updated = Counter()
    for stone, count in stones.items():
        if stone == 0:
            updated[1] += count
        else:
            stone_str = str(stone)
            stone_len = len(stone_str)
            if stone_len % 2 == 0:
                mid = stone_len // 2
                updated[int(stone_str[:mid])] += count
                updated[int(stone_str[mid:])] += count
            else:
                updated[stone * 2024] += count
    return updated
