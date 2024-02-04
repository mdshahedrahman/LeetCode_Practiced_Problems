from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            # Extract digits from the current nodes of l1 and l2
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum and carry
            total_sum = val1 + val2 + carry
            carry = total_sum // 10
            current.next = ListNode(total_sum % 10)

            # Move to the next nodes if available
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            current = current.next

        return dummy_head.next


# Helper function to convert ListNode to list
def convert_linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Your existing code
solution = Solution()
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

result = solution.addTwoNumbers(l1, l2)

# Convert the result to a list and print
result_list = convert_linked_list_to_list(result)
print(result_list)