# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # not in-place solution (O(1) memory). 

        # helper function for reverse-LL        
        def reverse(head):
            prev = None
            curr = head
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev # head 

        # get k groups together
        k_groups = [] # values: [start, end] nodes for each group. 
        curr, l_curr = head, head
        count = 1
        additional_nodes = None 
        while curr:
            if(count == k):
                count = 1
                temp = curr.next
                curr.next, additional_nodes = None, None
                k_groups.append([l_curr, curr])
                l_curr, curr = temp, temp

            else:
                curr = curr.next
                count += 1
                additional_nodes = l_curr


        # reverse each group in k_groups and replace with reversed LL
        for idx, group in enumerate(k_groups):
            k_groups[idx] = reverse(group[0])
        
        # if there are more nodes to add at end. 
        if(additional_nodes):
            k_groups.append(additional_nodes)

        # reconnect each group. 
        while(len(k_groups) > 1):
            first_group = k_groups.pop(0)
            
            # get to last element in reversed LL
            tail = first_group
            while tail.next:
                tail = tail.next

            # re-link            
            tail.next = k_groups.pop(0)
            k_groups.insert(0, first_group)

        return k_groups[0]
