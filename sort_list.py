# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
        res, ptr, tem, i = A, A, [], 0
        if not A or not A.next:
            return A
        while ptr:
            tem.append(ptr.val)
            ptr = ptr.next
        tem.sort()
        ptr = res
        while ptr:
            ptr.val, ptr = tem[i], ptr.next
            i += 1
        return res