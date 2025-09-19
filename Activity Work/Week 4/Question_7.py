from Question_1 import LinkedList
'''
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def Display(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        
    def Append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node
'''    

def FindFromEnd(linklist: LinkedList, n: int) -> int:
    if n <= 1 or not linklist.head:
        return 
    
    slow = linklist.head
    fast = linklist.head
    count = 0

    while count < n:
        if not fast:
            return 
        fast = fast.next
        count += 1

    while fast:
        slow = slow.next
        fast = fast.next

    return slow.data

def SecondLast(linklist: LinkedList) -> int:
    if not linklist.head or not linklist.head.next:
        return 
    
    current = linklist.head

    while current.next.next:
        current = current.next

    return current.data

# TestCase 1  ------------------->
print()
l1 = LinkedList()
data = [2, 4, 6, 8, 33, 67]
for i in data:
    l1.Append(i)

l1.Display()
print(f"The Second-Last Element is: {SecondLast(l1)}\n")

# TestCase 2  ------------------->
print()
l2 = LinkedList()
for i in range(1, 6):
    l2.Append(i)

l2.Display()
print(f"The Second-Last Element is: {SecondLast(l2)}\n")

# TestCase 3  ------------------->
print()
l3 = LinkedList()
for i in range(1, 2):
    l3.Append(i)

l3.Display()
print(f"The Second-Last Element is: {SecondLast(l3)}\n")

# Optional TestCase for FindFromEnd  ------------------->
print('------' * 10)
l4 = LinkedList()
for i in range(1, 11):
    l4.Append(i)

l4.Display()
n = 3
print(f"The {n}-th Element from the end is: {FindFromEnd(l4, n)}\n")