# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def solve(self, A, B):
        count, ptr, res = 0, A, None
        while ptr != None and count < B:
            count += 1
            res, ptr.next, ptr = ptr, res, ptr.next
        if A:
            A.next = ptr
        count = 0
        while count < B - 1 and ptr != None:
            count += 1
            ptr = ptr.next
        if ptr:
            ptr.next = self.solve(ptr.next, B)
        return res