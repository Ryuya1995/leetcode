# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from queue import PriorityQueue
        dum = curr = ListNode(0)
        q = PriorityQueue()
        for node in lists:
            if node:
                q.put((node.val, node))
        while q.qsize():
            curr.next = curr = q.get()[1]
            if curr.next:
                q.put((curr.next.val, curr.next))
        return dum.next





