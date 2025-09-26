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


def result(head):
    if not head:
        return 0

    # Step 1: Find the middle of the linked list
    slow = head
    fast = head
    stack = []

    while fast and fast.next:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    result = 0
    while slow:
        twin_sum = slow.data + stack.pop()
        result = max(result, twin_sum)
        slow = slow.next

    return result


# Testcase 1
l1 = LinkedList()
for i in range(1, 6):
    l1.Append(i)

l1.Display()
print("Max Twin Sum:", result(l1.head))
print('--' * 50)

# Testcase 2
l2 = LinkedList()
for i in [4, 2, 2, 3]:
    l2.Append(i)

l2.Display()
print("Max Twin Sum:", result(l2.head))

