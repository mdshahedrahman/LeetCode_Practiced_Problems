# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        unique_values = set()
        unique_head = ListNode()
        current = unique_head

        while head:
            if head.val not in unique_values:
                unique_values.add(head.val)
                current.next = ListNode(head.val)
                current = current.next

            head = head.next

        return unique_head.next