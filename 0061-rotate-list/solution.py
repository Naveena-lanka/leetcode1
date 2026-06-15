# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Find length and last node
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Reduce unnecessary rotations
        k = k % length

        if k == 0:
            return head

        # Make circular list
        tail.next = head

        # Find new tail position
        steps = length - k

        new_tail = head

        for i in range(steps - 1):
            new_tail = new_tail.next

        # New head is after new tail
        new_head = new_tail.next

        # Break circle
        new_tail.next = None

        return new_head
        
