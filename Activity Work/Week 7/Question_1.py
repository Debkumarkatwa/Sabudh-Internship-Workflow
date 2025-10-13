class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
    if not head or left == right:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    # Move prev to the node before the left position
    for _ in range(left - 1):
        prev = prev.next

    # Reverse the sublist
    curr = prev.next
    for _ in range(right - left):
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp

    return dummy.next

# Example usage:
if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    left, right = 2, 4
    new_head = reverseBetween(head, left, right)
    while new_head:
        print(new_head.val, end=" -> ")
        new_head = new_head.next

    print()

    head = ListNode(5)  # Single node list
    left, right = 1, 1
    new_head = reverseBetween(head, left, right)
    while new_head:
        print(new_head.val, end=" -> ")
        new_head = new_head.next