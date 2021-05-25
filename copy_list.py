from collections import defaultdict as dedt
    
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        dd = dedt(lambda: RandomListNode(0))
        dd[None], ptr = None, head
        while ptr :
            dd[ptr].label, dd[ptr].next, dd[ptr].random = ptr.label, dd[ptr.next], dd[ptr.random]
            ptr = ptr.next
        return dd[head]