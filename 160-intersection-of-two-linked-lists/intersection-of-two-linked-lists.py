# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None

        pA, pB = headA, headB

        while pA != pB:
            # Move forward, or jump to the other list’s head
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA

        return pA  # Either intersection node or None
