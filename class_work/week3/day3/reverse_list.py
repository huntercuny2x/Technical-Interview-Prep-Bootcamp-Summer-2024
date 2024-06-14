class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    p1, p2 = None, head
    while  p2:
        p3 = p2.next
        p2.next = p1
        p1 = p2
        p2 = p3
    
    return p1