class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: list):
    def mergeTwoLists(l1, l2):
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 if l1 else l2
        return dummy.next

    if not lists:
        return None
    
    Ll = 1
    n = len(lists)
    while Ll < n:
        for i in range(0, n - Ll, Ll * 2):
            lists[i] = mergeTwoLists(lists[i], lists[i + Ll])
        Ll *= 2
    return lists[0] if n > 0 else None

# Example usage:
lists = [
    ListNode(1, ListNode(4, ListNode(5))),
    ListNode(1, ListNode(3, ListNode(4))),
    ListNode(2, ListNode(6))
]
merged = mergeKLists(lists)
while merged:
    print(merged.val, end=" -> " if merged.next else "")
    merged = merged.next