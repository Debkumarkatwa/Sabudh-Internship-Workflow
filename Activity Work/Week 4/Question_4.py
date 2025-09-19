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

def Reverse(linklist: LinkedList):
    prev = None
    current = linklist.head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    linklist.head = prev

# TestCase 1  ------------------->
print()
l1 = LinkedList()
for i in range(1, 5):
    l1.Append(i)

l1.Display()
Reverse(l1)

print("After Reversing the Linked List:\n\t", end="")
l1.Display()

# TestCase 2  ------------------->
print()
l2 = LinkedList()
for i in range(1, 6):
    l2.Append(i)

l2.Display()
Reverse(l2)

print("After Reversing the Linked List:\n\t", end="")
l2.Display()

# TestCase 3  ------------------->
print()
l3 = LinkedList()
l3.Append(1)

l3.Display()
Reverse(l3)

print("After Reversing the Linked List:\n\t", end="")
l3.Display()