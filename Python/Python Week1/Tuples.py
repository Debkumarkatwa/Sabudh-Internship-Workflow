# 1. Write a Python program to create a tuple with different data types.
def Tuple_Create(*args) -> tuple:
    return tuple(args)

# 2. Write a Python program to create a tuple of numbers and print one item. 
def Print_Item(Tuple:tuple, index:int) -> any:
    if index < 0 or index >= len(Tuple):
        return None
    return Tuple[index]

# 3.   Write a Python program to add an item to a tuple. 
def Tuple_Add(Tuple:tuple, item:any) -> tuple:
    return Tuple + (item,)

# 4.  Write a Python program to get the 4th element from the last element of a Tuple. 
def Fourth_From_Last(Tuple:tuple) -> any:
    if len(Tuple) < 4:
        return None
    return Tuple[-4]

# 5.  Write a Python program to convert a tuple to a dictionary. 
def Tuple_To_Dict(Tuple:tuple) -> dict:
    if not Tuple:
        return {}
    result = dict()
    for i, value in enumerate(Tuple):
        result[i] = value

    return result

'''
6.  Write a Python program to replace the last value of tuples in a list. 
    Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)] 
    Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
'''
def Replace_Last_Value(Tuple_List:list, new_value:any) -> list:
    if not Tuple_List:
        return []
    if not type(Tuple_List[0][0]) == type(new_value):
        return 'Invalid input type for new_value'

    result = []
    for t in Tuple_List:
        if len(t) < 1:
            result.append(t)
        else:
            new_tuple = t[:-1] + (new_value,)
            result.append(new_tuple)

    return result

print(Tuple_Create(1,2,3,4,5))

# Test cases for Print_Item function
print("\nTesting Print_Item function:")
tuple_print = (1, 2, 3, 4, 5)
print(f"Test case 1: Print_Item({tuple_print}, 2) ->\n\t\t {Print_Item(tuple_print, 2)}") # Valid index
print(f"Test case 2: Print_Item({tuple_print}, -1) ->\n\t\t {Print_Item(tuple_print, -1)}") # Negative index
print(f"Test case 3: Print_Item({tuple_print}, 10) ->\n\t\t {Print_Item(tuple_print, 10)}") # Index out of bounds


# Test cases for Tuple_Add function
print("\nTesting Tuple_Add function:")
tuple_add = (1, 2, 3)
print(f"Original tuple: {tuple_add}")
new_tuple1 = Tuple_Add(tuple_add, 4)
print(f"Test case 1: Tuple_Add({tuple_add}, 4) ->\n\t\t {new_tuple1}")

new_tuple2 = Tuple_Add(tuple_add, "hello")
print(f"Test case 2: Tuple_Add({tuple_add}, 'hello') ->\n\t\t {new_tuple2}")


# Test cases for Fourth_From_Last function
print("\nTesting Fourth_From_Last function:")
tuple_fourth1 = (1, 2, 3, 4)
print(f"Test case 1: Fourth_From_Last({tuple_fourth1}) ->\n\t\t {Fourth_From_Last(tuple_fourth1)}")

tuple_fourth2 = (1, 2, 3, 4, 5, 6)
print(f"Test case 2: Fourth_From_Last({tuple_fourth2}) ->\n\t\t {Fourth_From_Last(tuple_fourth2)}")

tuple_fourth3 = (1, 2, 3)
print(f"Test case 3: Fourth_From_Last({tuple_fourth3}) ->\n\t\t {Fourth_From_Last(tuple_fourth3)}")

tuple_fourth4 = ()
print(f"Test case 4: Fourth_From_Last({tuple_fourth4}) ->\n\t\t {Fourth_From_Last(tuple_fourth4)}")


# Test cases for Tuple_To_Dict function
print("\nTesting Tuple_To_Dict function:")
tuple_dict1 = (("a", 1), ("b", 2), ("c", 3))
print(f"Test case 1: Tuple_To_Dict({tuple_dict1}) ->\n\t\t {Tuple_To_Dict(tuple_dict1)}")

tuple_dict2 = (("x", 10), ("y", 20), ("z", 30))
print(f"Test case 2: Tuple_To_Dict({tuple_dict2}) ->\n\t\t {Tuple_To_Dict(tuple_dict2)}")


# Test cases for Replace_Last_Value function
print("\nTesting Replace_Last_Value function:")

tuple_list1 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
new_value1 = 10
print(f"Test case 1: Replace_Last_Value({tuple_list1}, {new_value1}) ->\n\t\t {Replace_Last_Value(tuple_list1, new_value1)}")

tuple_list2 = [(1, 2), (), (3, 4)]
new_value2 = 5
print(f"Test case 2: Replace_Last_Value({tuple_list2}, {new_value2}) ->\n\t\t {Replace_Last_Value(tuple_list2, new_value2)}")

tuple_list3 = []
new_value3 = 100
print(f"Test case 3: Replace_Last_Value({tuple_list3}, {new_value3}) ->\n\t\t {Replace_Last_Value(tuple_list3, new_value3)}")