class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        tem1, tem2, k, ptr, res = A, B, 0, ListNode(0), ListNode(0)
        res = ptr
        while tem1 or tem2 or k:
            if tem1:
                k += tem1.val
                tem1 = tem1.next
            if tem2:
                k += tem2.val
                tem2 = tem2.next
            ptr.next = ListNode(k % 10)
            ptr, k = ptr.next, k // 10
        return res.next