"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # edge case 
        if(head == None):
            return None

        # first while loop stores key:val pair of idx:val (val of a node) in the in_order_hash
        # & stores key:val pair of node:idx in reverse_hash 
        in_order_hash = {}
        reverse_hash = {}
        curr = head
        idx = 0
        while curr:
            in_order_hash[idx] = curr.val
            reverse_hash[curr] = idx
            curr=curr.next
            idx+=1

        # second while loop creates in-order list to store random indices, or -1 if Null  
        in_order_rand_idxs = []
        curr2 = head
        while curr2:
            if(curr2.random != None):
                in_order_rand_idxs.append(reverse_hash[curr2.random])
            else:
                in_order_rand_idxs.append(-1)
            curr2=curr2.next
        
        # first for loop constructs deepcopy linked list (without random pointers)
        dummy_node = Node(0)
        cpy_node = dummy_node
        rand_hash = {} # stores idx:node 
        for idx_ in range(0, idx):
            cpy_node.val = in_order_hash[idx_]
            cpy_node.next = Node(0)
            rand_hash[idx_] = cpy_node
            cpy_node=cpy_node.next

        # second for loop adds random pointer for each node in linked list deepcopy. 
        cpy_rand_node = dummy_node
        for idx__ in range(0, len(in_order_rand_idxs)):
            if(in_order_rand_idxs[idx__] == -1):
                cpy_rand_node.random = None
            else:
                cpy_rand_node.random = rand_hash[in_order_rand_idxs[idx__]]
            if(idx__ == len(in_order_rand_idxs) - 1):
                cpy_rand_node.next = None
                break
            else:
                cpy_rand_node=cpy_rand_node.next
        return dummy_node
