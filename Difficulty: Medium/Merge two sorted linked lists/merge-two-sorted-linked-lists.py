'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

'''
class Solution:
    # Function to merge two sorted linked lists
    def sortedMerge(self, head1, head2):
        
        dummy = Node(0)   # Dummy node
        tail = dummy
        
        # Traverse both lists
        while head1 and head2:
            
            if head1.data <= head2.data:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            
            tail = tail.next
        
        # If elements remain in list1
        if head1:
            tail.next = head1
        
        # If elements remain in list2
        if head2:
            tail.next = head2
        
        return dummy.next               
   