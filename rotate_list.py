# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        head, count = A, 0
        while head:
            head = head.next
            count += 1
        B %= count
        if B == 0:
            return A
        n, m = count - B, 1
        tem = head = A
        while head and m <= n:
            tem, head = head, head.next
            m += 1
        tem.next, ptr = None, head
        while head.next:
            head = head.next
        head.next = A
        return ptr