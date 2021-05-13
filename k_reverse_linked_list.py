#Definition for singly-linked list.
#class ListNode:
#def init(self, x):
#   self.val = x
#   self.next = None
class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, A, B):
        head = A
        while head:
            temp, ptr, k  = [], head, B
            while k > 0 and head:
                temp.append(head.val)
                head, k = head.next, k - 1
            k = B - 1
            while k > -1 and ptr:
                ptr.val, ptr, k = temp[k], ptr.next, k - 1
            head = ptr
        return A