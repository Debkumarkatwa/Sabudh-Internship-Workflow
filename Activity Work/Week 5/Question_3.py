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


def Marge_Two_Sorted_Linked_Lists(l1, l2):
    temp = Node(0)
    tail = temp        

    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    return temp.next

# Testcase 1
l1 = LinkedList()
for i in [1, 2, 4]:
    l1.Append(i)

l2 = LinkedList()
for i in [1, 3, 4]:
    l2.Append(i)

l1.Display()
l2.Display()
merged_head = Marge_Two_Sorted_Linked_Lists(l1.head, l2.head)
merged_list = LinkedList()
merged_list.head = merged_head
merged_list.Display()

print('--' * 50)
# Testcase 2
l3 = LinkedList()
l3.Display()
l4 = LinkedList()
l4.Display()

marged_head2 = Marge_Two_Sorted_Linked_Lists(l3.head, l4.head)
merged_list2 = LinkedList()
merged_list2.head = marged_head2
merged_list2.Display()