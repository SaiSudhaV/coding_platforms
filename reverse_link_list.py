# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, A):
        if A == None or A.next == None:
            return A
        head = self.reverseList(A.next)
        A.next.next = A
        A.next = None
        return head