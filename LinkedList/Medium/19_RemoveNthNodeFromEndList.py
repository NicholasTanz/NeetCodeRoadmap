# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #find num of nodes with 1st while loop
        curr = head
        num_nodes=0 
        while curr:
            num_nodes+=1
            curr=curr.next
        nth_node_front = num_nodes - n

        # edge cases
        if(num_nodes == 1):
            return None
        elif(nth_node_front == 0):
            return head.next

      # locate node, to then skip nxt node, then point to nxt nxt node. 
        find_node = head
        num_nodes=0
        while(num_nodes < nth_node_front-1):
            find_node=find_node.next
            num_nodes+=1

        if(find_node and find_node.next):
            find_node.next = find_node.next.next
        
        return head
