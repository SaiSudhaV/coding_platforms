# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        head = A
        while head and head.next:
            temp = head.next
            head.val, temp.val, head = temp.val, head.val, temp.next
        return A