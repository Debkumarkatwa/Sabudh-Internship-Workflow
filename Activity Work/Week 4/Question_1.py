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

    def FindMiddle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data if slow else None


if __name__ == "__main__":
    # TestCase 1  
    l1 = LinkedList()
    for i in range(1, 6):
        l1.Append(i)
        
    l1.Display()

    print(f"The Middle Element is: {l1.FindMiddle()}\n")


    # TestCase 2
    l2 = LinkedList()
    for i in range(1, 7):
        l2.Append(i)
        
    l2.Display()

    print(f"The Middle Element is: {l2.FindMiddle()}\n")

    # TestCase 3
    l3 = LinkedList()
    # l3.Append(1)
    l3.Display()
    print(f"The Middle Element is: {l3.FindMiddle()}\n")