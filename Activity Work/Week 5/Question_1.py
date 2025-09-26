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

def insert_begining(head, value):
    new_node = Node(value)
    new_node.next = head
    return new_node

# Testcase 1
l1 = LinkedList()
for i in range(2, 6):
    l1.Append(i)
l1.Display()

l1.head = insert_begining(l1.head, 1)
l1.Display()

print('--' * 50)
# Testcase 2
l2 = LinkedList()
for i in [3, 2, 5, 7, 1, 2]:
    l2.Append(i)
l2.Display()

l2.head = insert_begining(l2.head, 10)
l2.Display()