class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        if A.next == None:
            return A
        else:
            res = ListNode(-1)
            res.next, temp, ptr = A, res, A
            while ptr.val < B:
                ptr, temp = ptr.next, temp.next
            p = temp
            while ptr:
                if ptr.val < B:
                    temp.next, ptr.next, p.next = ptr.next, p.next, ptr
                    p, ptr = ptr, temp.next
                else:
                    ptr, temp = ptr.next, temp.next
        res = res.next
        return res