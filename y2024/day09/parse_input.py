"""
Advent of Code 2024
Day 09
Sebastian Altomare

Parse Input
"""
from pathlib import Path
FREE = "."

def parse_input(file_name):
    """
    Parses a text file to generate a list representing disk blocks, which are 
    either a numbered file block or a free block.
    
    Args:
        file_name (str): The path or name of the file to read.
        
    Returns:
        List[int | str]: A list of file blocks.
    """
    path = Path(file_name)
    with path.open("r", encoding="utf-8") as file:
        disk_map = file.read().strip()


    blocks, file_id = [], 0
    for file_block, free_block in zip(disk_map[::2], disk_map[1::2]):
        blocks.extend([file_id] * int(file_block))
        blocks.extend([FREE] * int(free_block))
        file_id += 1
    if len(disk_map) % 2 != 0:
        blocks.extend([file_id] * int(disk_map[-1]))
    return blocks
