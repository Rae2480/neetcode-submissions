# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        # while loop continues as long as fast has 2 more nodes to traverse, incl itself
        # next traversal might contain null at which point while loop ends
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            # take note that fast & slow are the variables 
            # they hold the information so they are the ones we must modify

            if fast == slow:
                return True
            # check must be after pointers have started moving since they both start from same head
        
        return False

