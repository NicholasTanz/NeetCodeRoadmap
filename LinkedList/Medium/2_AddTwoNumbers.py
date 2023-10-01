# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      #edge case  
      if(not l1 and not l2):
            return None
        # first two while loops create array of nums for l1 & l2
        curr_l1 = l1
        curr_l2 = l2
        ary_l1 = []
        ary_l2 = []
        l1_len = 0
        l2_len = 0
        while(curr_l1):
            ary_l1.append(curr_l1.val)
            curr_l1=curr_l1.next
            l1_len+=1
        while(curr_l2):
            ary_l2.append(curr_l2.val)
            curr_l2=curr_l2.next
            l2_len+=1

        # this for loop calculates sum for elements in l1 & l2 - where l1 & l2 elements share same indices (min utilized).
        sum_ary_forward = []
        sum_ary_len=0
        min_l = l1_len if l2_len > l1_len else l2_len
        max_l = l1_len if l2_len < l1_len else l2_len
        extra_one = False
        for i in range(0, min_l):
            if(ary_l1[i] + ary_l2[i] >= 10):
                if(i+1 < min_l):
                    ary_l1[i+1]+=1
                else:
                    extra_one = True
            sum_ary_forward.append((ary_l1[i] + ary_l2[i]) % 10)
            sum_ary_len+=1
        
        # accounts for extra element sin either l1 or l2; and adds to sum ary as needed
        use_ary = ary_l1 if max_l == l1_len else ary_l2
        extra = False
        for i in range(min_l, max_l):
            if(extra_one):
                use_ary[i]+=1
                extra_one = False
                kp_incr = i
                # continues to search longer ary, if element is >= 10, adds +1 to nxt element
                while(use_ary[kp_incr] >= 10):
                    use_ary[kp_incr]%=10
                    kp_incr+=1
                    if(kp_incr >= max_l):
                        extra = True
                        break
                    use_ary[kp_incr]+=1

            sum_ary_forward.append(use_ary[i])
            sum_ary_len+=1

        # case where last digit is overflowed and extra 1 is needed (hence extra & extra_one vars)
        if(extra or extra_one):
            sum_ary_forward.append(1)
            sum_ary_len+=1
          
        #creating return linked list
        ret_node = ListNode()
        ret_node.val = sum_ary_forward[0]
        curr = ret_node
        for i in range(1, sum_ary_len):
            curr.next = ListNode(val=sum_ary_forward[i])
            curr=curr.next
        return ret_node
