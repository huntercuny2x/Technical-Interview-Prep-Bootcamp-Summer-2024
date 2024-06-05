# Given a list of integers, remove any nodes that have values that have 
# previously occurred in the list and return a reference to the head of the 
# list.

###############################################################################
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


###############################################################################
def condense(head):
    duplicate_map = {}

    prev = ListNode(0,head)
    curr = head
    while curr:
        duplicate_map[curr.val]=duplicate_map.get(curr.val,0)+1

        if duplicate_map[curr.val] > 1:
            prev.next = curr.next
            curr=prev.next
        
        else:
            prev=prev.next
            curr=curr.next
    return head


###############################################################################
def arrayToLinkedList(arr):
    dummy=ptr=ListNode()
    for a in arr:
        ptr.next=ListNode(a,None)
        ptr =ptr.next
    return dummy.next


###############################################################################
def printLinkedList(head):
    ptr = head
    while ptr:
        print(ptr.val)
        ptr=ptr.next


#test 1
###############################################################################
# head1=arrayToLinkedList([3,4,3,6])
# printLinkedList(head1)
# print()
# head2=condense(head1)
# printLinkedList(head2)


#test 2
###############################################################################
head1=arrayToLinkedList( [ 3, 4, 3, 2, 6, 1, 2, 6 ])
printLinkedList(head1)
print()
head2=condense(head1)
printLinkedList(head2)
# space O(1), time: O(n)