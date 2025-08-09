# 1  Write a Python script to sort (ascending and descending) a dictionary by value. 
def Sort_Dict_By_Value(d: dict, ascending: bool = True) -> dict:
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=not ascending))

# 2. Write a Python program to iterate over dictionaries using for loops. 
def Iterate_Dict(d: dict) -> None:
    for key, value in d.items():
        print(f"{key}: {value}")

# 3. Write a Python script to merge two Python dictionaries. 
def Merge_Dicts(dict1: dict, dict2: dict) -> dict:
    merged_dict = dict1.copy()  # Create a copy of the first dictionary
    merged_dict.update(dict2)   # Update it with the second dictionary

    return merged_dict

# 4. Write a Python program to sum all the items in a dictionary. 
def Sum_Dict_Items(d: dict) -> any:
    if not d:
        return 0
    
    total = 0

    for value in d.values():
        total += value
        
    return total

# 5. Write a Python program to multiply all the items in a dictionary. 
def Multiply_Dict_Items(d: dict) -> any:
    if not d:
        return 1
    
    product = 1

    for value in d.values():
        product *= value
        
    return product

# 6. Write a Python program to sort a given dictionary by key. 
def Sort_Dict_By_Key(d: dict, ascending: bool = True) -> dict:
    return dict(sorted(d.items(), key=lambda item: item[0], reverse=not ascending))

# 7. Write a Python program to remove duplicates from the dictionary. 
def Remove_Dict_Duplicates(d: dict) -> dict:
    seen = set()
    result = dict()
    
    for key, value in d.items():
        if value not in seen:
            seen.add(value)
            result[key] = value
            
    return result


# Test cases for Sort_Dict_By_Value
print("Testing Sort_Dict_By_Value:")
d1 = {'a': 3, 'b': 1, 'c': 2}
print(f"Original: {d1}")
print(f"Ascending: {Sort_Dict_By_Value(d1)}")
print(f"Descending: {Sort_Dict_By_Value(d1, ascending=False)}")
print("-" * 20)

# Test cases for Iterate_Dict
print("Testing Iterate_Dict:")
d2 = {'x': 10, 'y': 20, 'z': 30}
print("Iterating through the dictionary:")
Iterate_Dict(d2)
print("-" * 20)

# Test cases for Merge_Dicts
print("Testing Merge_Dicts:")
d3 = {'a': 1, 'b': 2}
d4 = {'c': 3, 'd': 4}
print(f"Dict 1: {d3}")
print(f"Dict 2: {d4}")
print(f"Merged: {Merge_Dicts(d3, d4)}")
print("-" * 20)

# Test cases for Sum_Dict_Items
print("Testing Sum_Dict_Items:")
d5 = {'a': 10, 'b': 20, 'c': 30}
print(f"Dictionary: {d5}")
print(f"Sum: {Sum_Dict_Items(d5)}")
print(f"Empty dictionary sum: {Sum_Dict_Items({})}")
print("-" * 20)

# Test cases for Multiply_Dict_Items
print("Testing Multiply_Dict_Items:")
d6 = {'a': 2, 'b': 3, 'c': 4}
print(f"Dictionary: {d6}")
print(f"Product: {Multiply_Dict_Items(d6)}")
print(f"Empty dictionary product: {Multiply_Dict_Items({})}")
print("-" * 20)

# Test cases for Sort_Dict_By_Key
print("Testing Sort_Dict_By_Key:")
d7 = {'c': 3, 'a': 1, 'b': 2}
print(f"Original: {d7}")
print(f"Ascending: {Sort_Dict_By_Key(d7)}")
print(f"Descending: {Sort_Dict_By_Key(d7, ascending=False)}")
print("-" * 20)

# Test cases for Remove_Dict_Duplicates
print("Testing Remove_Dict_Duplicates:")
d8 = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
print(f"Original: {d8}")
print(f"Without duplicates: {Remove_Dict_Duplicates(d8)}")
print("-" * 20)