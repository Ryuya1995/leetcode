# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or k == 1:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        i = 0
        while head != None:
            i += 1
            if i % k == 0:
                pre = self.reverse(pre, head.next)
                head = pre.next
            else:
                head = head.next
        return dummy.next

    def reverse(self, pre, next):
        """
        * Reverse a link list between pre and next exclusively
        * an example:
        * a linked list:
        * 0->1->2->3->4->5->6
        * |           |
        * pre        next
        * after call pre = reverse(pre, next)
        *
        * 0->3->2->1->4->5->6
        *          |  |
        *          pre next
        """
        last = pre.next
        cur = last.next
        while cur != next:
            last.next = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = last.next
        return last
