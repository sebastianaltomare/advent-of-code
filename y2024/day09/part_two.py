"""
Advent of Code 2024
Day 09
Sebastian Altomare

Part Two
"""
from parse_input import parse_input
FREE = "."

def whole_block_checksum(file_name):
    """
    Computes the checksum of a file system without fragmentation.
    
    Args:
        file_name (str): The path or name of the file to read.
    
    Returns:
        int: The checksum of the file system.
    """
    blocks = parse_input(file_name)
    maximum_id = max(block for block in blocks if block != FREE)

    for file_id in range(maximum_id, -1, -1):
        move_file_block(blocks, file_id)

    return sum(i * value for i, value in enumerate(blocks) if value != FREE)


def move_file_block(blocks, file_id):
    """
    Moves a file_block to the next available contiguous space if possible.
    
    Args:
        blocks (List[int | str]): A list of file blocks.
        id (int): The id of the file block trying to be moved.
    
    Returns:
        None: Updates the blocks list in place if possible.
    """
    start = None
    length = 0
    for i, block in enumerate(blocks):
        if block == file_id:
            length += 1
            if start is None:
                start = i

    if start is not None:
        target = find_first_open_space(blocks, start, length)
        if target is not None:
            blocks[start : start + length] = [FREE] * length
            blocks[target : target + length] = [file_id] * length


def find_first_open_space(blocks, index, length):
    """
    Determines the first open space possible to move a file block.

    Args:
        blocks (List[int | str]): A list of file blocks.
        index (int): The index of the given file block in the file system.
        length (int): The length of the given file block.
        
    Returns:
        int | None: The index of the free space if exists, else None.
    """
    current_length = 0
    start = None
    for i in range(index):
        if blocks[i] == FREE:
            if start is None:
                start = i
            current_length += 1
            if current_length >= length:
                return start
        else:
            current_length = 0
            start = None
    return None
