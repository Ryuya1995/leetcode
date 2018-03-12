# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def print(self):
        a=self
        while a:
            print(a.val, end="")
            a=a.next
        print()


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        tail = head
        n = 1
        while tail.next:
            n += 1
            tail = tail.next
        tail.next = head
        tmp = head
        k = k % n
        for _ in range(n-k-1):
            tmp = tmp.next
        res = tmp.next
        tmp.next = None
        return res

li = ListNode(1)
li.next = ListNode(2)
li.next.next = ListNode(3)
li.next.next.next = ListNode(4)
li.next.next.next.next=ListNode(5)
Solution().rotateRight(li,6).print()
