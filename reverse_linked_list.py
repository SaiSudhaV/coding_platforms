class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def reverseList(self, A):
	    temp, head = None, A
        while head.next:
            head.next, temp, head = temp, head, head.next
        head.next = temp
        return head