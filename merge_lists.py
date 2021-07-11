# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from heapq import heapify, heappop, heappush

class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        tem, n = [], len(A)
        for i in range(n):
            heappush(tem, (A[i].val, A[i].next))
        k, next_ele = heappop(tem)
        res = ptr = ListNode(k)
        if next_ele:
            heappush(tem, (next_ele.val, next_ele.next))
        while tem:
            k, next_ele = heappop(tem)
            if next_ele:
                heappush(tem, (next_ele.val, next_ele.next))
            new_node = ListNode(k)
            ptr.next, ptr = new_node, new_node
        return res