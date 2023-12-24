from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current is not None:
            next_node = current.next  # Save the next node
            current.next = prev  # Reverse the link
            prev = current  # Move to the next pair of nodes
            current = next_node

        head = prev  # The last node becomes the new head
        return head
