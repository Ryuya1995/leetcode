# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # def print(self):
    #     a=self
    #     while a:
    #         print(a.val, end="")
    #         a=a.next
    #     print()
    #
    # def reverseList(self):
    #     L = ListNode(None)
    #     while self:
    #         L.next, self.next, self = self, L.next, self.next
    #         # a=self ; b=L.next ; c=self.next
    #         # L.next = self
    #         # self.next = b  #Here，L.next=b
    #         # self = c
    #     return L.next


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        l3 = l4 = ListNode(0) #add=l3=l4
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, val = divmod(carry,10)
            l3.next = ListNode(val) #add.next=l3.next
            l3 = l3.next  #add=add.next
        return l4.next


# l1 = ListNode(3)
# l1.next = ListNode(4)
# l2 = ListNode(5)
# l2.next = ListNode(6)
# s=Solution()
# s.addTwoNumbers(l1,l2).reverseList().print()





