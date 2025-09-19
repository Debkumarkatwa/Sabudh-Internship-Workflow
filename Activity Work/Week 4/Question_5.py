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

def ConvertToLL(Num) -> LinkedList:
    '''
    I am Unable to understand the INPUT properly. If it is given in NUMBER then ok.
    Otherwise if it is given in LINKED LIST format then I need to convert it in NUMBER. 
    So, I have implemented that too.
    '''
    if isinstance(Num, LinkedList):
        num = 0
        current = Num.head
        while current:
            num = num * 10 + current.data
            current = current.next

        Num = num

    Num = abs(Num) + 1
    linklist = LinkedList()

    for value in str(Num):
        linklist.Append(int(value))

    return linklist

# TestCase 1  ------------------->
print()
l1 = ConvertToLL(1999)
l1.Display()

# TestCase 2  ------------------->
print()
l2 = ConvertToLL(3453)
l2.Display()


# Optional TestCase  ------------------->
print()
ll = LinkedList()
data = [9, 9, 9]
for value in data:
    ll.Append(value)

ll.Display()

ll = ConvertToLL(ll)
print("After Adding One: \n\t", end="")
ll.Display()