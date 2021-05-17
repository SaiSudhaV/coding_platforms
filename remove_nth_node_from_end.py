# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        tem, res = A, 1
        while tem.next != None:
            tem, res, p = tem.next, res + 1, res - B + 1
        if B < res:
            ptr = A
        else:
            A = A.next
            return A
        for i in range(1, res):
            if i != p:
                ptr = ptr.next
            else:
                ptr.next = ptr.next.next
        return A