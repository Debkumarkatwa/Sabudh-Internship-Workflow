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

def RemoveDuplicate(linklist: LinkedList):
    current = linklist.head

    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

# TestCase 1  ------------------->
print()
l1 = LinkedList()
data = [11,11,11,21,43,43,60]
for value in data:
    l1.Append(value)

l1.Display()

RemoveDuplicate(l1)
print("After removing duplicates: \n\t", end="")
l1.Display()

# TestCase 2  ------------------->
print()
l2 = LinkedList()
data = [10,15,15,15,20,20,20,23,25,25]
for value in data:
    l2.Append(value)
    
l2.Display()

RemoveDuplicate(l2)
print("After removing duplicates: \n\t", end="")
l2.Display()