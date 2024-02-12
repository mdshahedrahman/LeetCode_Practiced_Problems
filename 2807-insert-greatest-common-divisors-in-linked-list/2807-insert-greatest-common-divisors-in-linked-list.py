from typing import Optional
# Definition for singly-linked list.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Calculate greatest common divisors and insert into the linked list
        current = head
        while current and current.next:
            a, b = current.val, current.next.val
            common_divisor = gcd(a, b)

            # Insert the common divisor node
            new_node = ListNode(common_divisor)
            new_node.next = current.next
            current.next = new_node

            # Move to the next original node
            current = current.next.next

        return head
