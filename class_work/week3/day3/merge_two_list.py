class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    dummy = p =  ListNode()

    while list1 and list2:
        if list1.val < list2.val:
            p.next = list1
            list1=list1.next

        else:
            p.next = list2
            list2=list2.next
        p=p.next

    p.next = list1 or list2
    return dummy.next 

