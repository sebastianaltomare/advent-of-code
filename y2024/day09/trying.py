def parse_disk_map(disk_map):
    # Convert the disk map into a list of files and spaces
    chunks = []
    file_id = 0
    for i, length in enumerate(disk_map):
        length = int(length)
        if i % 2 == 0:  # File
            chunks.append(('file', length, file_id))
            file_id += 1
        else:  # Space
            chunks.append(('space', length))
    return chunks

def expand_to_blocks(chunks):
    # Convert chunks into individual blocks representation
    blocks = []
    for chunk in chunks:
        if chunk[0] == 'file':
            blocks.extend([chunk[2]] * chunk[1])  # File ID repeated length times
        else:
            blocks.extend(['.'] * chunk[1])  # Spaces
    return blocks

def calculate_checksum(blocks):
    # Calculate checksum by multiplying position by file ID for non-space blocks
    return sum(pos * file_id for pos, file_id in enumerate(blocks) if file_id != '.')

def find_leftmost_space(blocks, size_needed):
    # Find the leftmost span of contiguous free space that can fit the file
    current_span = 0
    start_of_span = 0
    
    for i, block in enumerate(blocks):
        if block == '.':
            if current_span == 0:
                start_of_span = i
            current_span += 1
            if current_span >= size_needed:
                return start_of_span
        else:
            current_span = 0
    return -1

def move_whole_file(blocks, file_id):
    # Find all blocks of this file (they might not be contiguous)
    file_positions = [i for i, block in enumerate(blocks) if block == file_id]
    if not file_positions:
        return False
        
    file_size = len(file_positions)
    leftmost_space = find_leftmost_space(blocks[:file_positions[0]], file_size)
    
    if leftmost_space == -1:
        return False
        
    # Remove file from current position
    for pos in file_positions:
        blocks[pos] = '.'
    
    # Insert at new position
    for i in range(file_size):
        blocks[leftmost_space + i] = file_id
        
    return True

def compact_disk_whole_files(disk_map):
    # Parse the input
    chunks = parse_disk_map(disk_map)
    blocks = expand_to_blocks(chunks)
    
    # Get unique file IDs in descending order
    file_ids = sorted(set(b for b in blocks if b != '.'), reverse=True)
    
    # Move each file once, starting from highest ID
    for file_id in file_ids:
        move_whole_file(blocks, file_id)
    
    return calculate_checksum(blocks)