from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Helper function to convert linked list to integer
        def list_to_int(node):
            result = 0
            while node:
                result = result * 10 + node.val
                node = node.next
            return result

        # Helper function to convert integer to reversed linked list
        def int_to_reversed_list(num):
            dummy = ListNode()
            current = dummy
            for digit in str(num)[::-1]:
                current.next = ListNode(int(digit))
                current = current.next
            return dummy.next

        # Convert linked lists to integers, add them, and convert back to a reversed linked list
        result_sum = list_to_int(l1) + list_to_int(l2)
        result_linked_list = int_to_reversed_list(result_sum)

        return result_linked_list