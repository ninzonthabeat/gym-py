from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_LL(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head

    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


class Solution:
    def addTwoNumbers(self,
                      l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        
        result = dummyHead.next
        dummyHead.next = None
        return result


solution = Solution()
# input: l1 = [2, 4, 3], l2 = [5, 6, 4]
l1_1 = list_to_LL([2, 4, 3])
l2_1 = list_to_LL([5, 6, 4])
# 342 + 465 = 807
result1 = solution.addTwoNumbers(l1_1, l2_1)

# output: [7, 0, 8]
while result1:
    print(result1.val, end=" -> ")
    result1 = result1.next
print()

# input: l1 = [0], l2 = [2]
l1_2 = ListNode(0)
l2_2 = ListNode(2)
result2 = solution.addTwoNumbers(l1_2, l2_2)
# output: [0]
while result2:
    print(result2.val, end=" -> ")
    result2 = result2.next
print()

# input: l1 = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]
l1_3 = list_to_LL([9, 9, 9, 9, 9, 9, 9, 9, 9, 9])
l2_3 = list_to_LL([9, 9, 9, 9])
result3 = solution.addTwoNumbers(l1_3, l2_3)
# output: [8, 9, 9 ,9, 0, 0, 0, 1]
while result3:
    print(result3.val, end=" -> ")
    result3 = result3.next
