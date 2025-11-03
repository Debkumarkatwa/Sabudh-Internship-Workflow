class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def removeNodes(self, head):
    if not head:
        return None
    
    def reverse(node):
        prev = None
        cur = node
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
    
    # Reverse, keep non-decreasing maxima, then reverse back
    head = reverse(head)
    dummy = ListNode(0)
    tail = dummy
    cur = head
    max_val = -10**9
    while cur:
        if cur.val >= max_val:
            max_val = cur.val
            tail.next = cur
            tail = cur
        cur = cur.next
    tail.next = None
    return reverse(dummy.next)


if __name__ == "__main__":
    head = ListNode(5, ListNode(2, ListNode(13, ListNode(3, ListNode(8)))))
    new_head = removeNodes(None, head)
    
    cur = new_head
    while cur:
        print(cur.val, end=" -> " if cur.next else "")
        cur = cur.next