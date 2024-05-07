# You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

# Return the head of the linked list after doubling it.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def twiceIt(self, head) -> int:
        if not head:
            return 0
        
        dual = head.val * 2 + self.twiceIt(head.next)
        head.val = dual % 10
        return dual // 10

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        carry = self.twiceIt(head)
        if carry:
            head = ListNode(carry, head)

        return head
             
        
    

        