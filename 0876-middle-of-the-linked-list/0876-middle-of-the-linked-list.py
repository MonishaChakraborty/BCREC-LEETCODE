# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Find length
        length = 0
        temp = head
        
        while temp:
            length += 1
            temp = temp.next
        
        # Step 2: Find middle index
        mid = length // 2
        
        # Step 3: Traverse to middle node
        temp = head
        for i in range(mid):
            temp = temp.next
        
        return temp