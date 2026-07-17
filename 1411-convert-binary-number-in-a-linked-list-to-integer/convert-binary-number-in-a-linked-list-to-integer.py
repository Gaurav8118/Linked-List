# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head):
        num = 0
        current = head
        while current:
            num = num * 2 + current.val   # shift left and add bit
            current = current.next
        return num
