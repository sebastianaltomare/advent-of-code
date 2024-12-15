"""
Advent of Code 2024
Day 1
Sebastian Altomare
"""

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
    list1 = []
    list2 = []
    for line in lines:
        data = line.split()
        first, second = data
        list1.append(int(first))
        list2.append(int(second))
    return list1, list2

def compute_total_distance(list1, list2):
    """
    Computes the distance between two lists and returns
    the result.
    
    Args:
        list1 (List[str]): The first list.
        list2 (List[str]): The second list.
    
    Returns:
        (int): The distance between the two lists.
    """
    list1.sort()
    list2.sort()
    distance = 0
    for i, value in enumerate(list1):
        distance += abs(value - list2[i])
    return distance

def compute_similarity_score(list1, list2):
    """
    Computes the similarity between two lists and returns
    the result.
    
    Args:
        list1 (List[str]): The first list.
        list2 (List[str]): The second list.
    
    Returns:
        (int): The similarity of two lists.
    """
    multiplicity_map = {}
    similarity_score = 0
    for value in list1:
        multiplicity_map[value] = multiplicity_map.get(value, 0) + 1
    for value in list2:
        similarity_score += value * multiplicity_map.get(value, 0)
    return similarity_score

def main():
    """
    Main Method
    """
    list1, list2 = read_input("./input.txt")
    distance = compute_total_distance(list1, list2)
    print(f"Distance: {distance}")

if __name__ == "__main__":
    main()
