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

def AddTwoLL(linklist1: LinkedList, linklist2: LinkedList) -> LinkedList:
    current_1 = linklist1.head
    current_2 = linklist2.head
    num1, num2 = 0, 0
    result_LL = LinkedList()

    while current_1 or current_2:
        if current_1:
            num1 = num1 * 10 + current_1.data
            current_1 = current_1.next

        if current_2:
            num2 = num2 * 10 + current_2.data
            current_2 = current_2.next

    total = num1 + num2
    for digit in str(total):
        result_LL.Append(int(digit))

    return result_LL

# TestCase 1  ------------------->
print()
l1 = LinkedList()
data = [5, 6, 3]
for i in data:
    l1.Append(i)

l2 = LinkedList()
data = [8, 4, 2]
for i in data:
    l2.Append(i)

result = AddTwoLL(l1, l2)

print("First Linked List: \n\t", end="")
l1.Display()
print("Second Linked List: \n\t", end="")
l2.Display()
print("Resultant Linked List after Addition: \n\t", end="")
result.Display()

# TestCase 2  ------------------->
print('------' * 10)
l3 = LinkedList()
data = [7, 5, 9, 4, 6]
for i in data:
    l3.Append(i)

l4 = LinkedList()
data = [8, 4]
for i in data:
    l4.Append(i)

result = AddTwoLL(l3, l4)

print("First Linked List: \n\t", end="")
l3.Display()
print("Second Linked List: \n\t", end="")
l4.Display()
print("Resultant Linked List after Addition: \n\t", end="")
result.Display()