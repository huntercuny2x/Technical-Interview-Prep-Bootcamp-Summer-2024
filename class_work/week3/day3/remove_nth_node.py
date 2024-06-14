class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    dummy=l=ListNode(0,head)
    r=head
    for i in range(n):
        r=r.next

    while r:
        r=r.next
        l=l.next
    
    l.next=l.next.next
    return dummy.next