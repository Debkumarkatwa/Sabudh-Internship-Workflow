class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head


# Example usage:
head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
print('Before removing duplicates:')
copy = head
while copy:
    print(copy.val, end=' -> ')
    copy = copy.next

head = deleteDuplicates(head)
print('\nAfter removing duplicates:')
while head:
    print(head.val, end=' -> ')
    head = head.next