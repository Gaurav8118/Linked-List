# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        # Step 1: Find middle (slow will end at mid)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Step 3: Compare first half and reversed second half
        left, right = head, prev
        while right:  # only need to check second half
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
