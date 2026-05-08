'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        #code here
        slow = head
        fast = head
        
        # Detect cycle using Floyd's Cycle Detection
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # Loop found
            if slow == fast:
                count = 1
                temp = slow.next
                
                # Count nodes in the loop
                while temp != slow:
                    count += 1
                    temp = temp.next
                
                return count
        
        # No loop
        return 0
                

        
        