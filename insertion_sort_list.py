class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        head, ptr, temp = ListNode(0), A, A
        head.next = A
        while temp:
            if ptr.val > temp.val:
                t1, t2, ptr.next = head, head.next, temp.next
                while t2 != None and temp.val > t2.val:
                    t1, t2 = t2, t2.next
                t1.next, temp.next, temp = temp, t2, ptr.next
            else:
                ptr, temp = temp, temp.next
        return head.next