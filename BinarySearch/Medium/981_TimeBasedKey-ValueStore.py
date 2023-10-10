class TimeMap:

    def __init__(self):
        self.valmap = {} # storing timestamp:value (to pull from after finding correct timestamp from findmap)
        self.findmap = {} # storing key:timestamp (utilized for binary search)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.findmap:
            self.findmap[key].append(timestamp)
            self.valmap[timestamp] = value
        else:
            self.findmap[key] = [timestamp]
            self.valmap[timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        # binary search
        if key in self.findmap:
            l_idx = 0
            check_lst = self.findmap[key]
            r_idx = len(check_lst) - 1
            m_idx = r_idx // 2
          
            # edge cases
            if(check_lst[0] > timestamp): 
                return ""
            if(r_idx <= 0):
                return self.valmap[check_lst[0]]
           
          # apply binary search - with condition that timestamp found must be closet to timestamp passed through get - but strictly less than or equal to. 
            while l_idx < r_idx and check_lst[l_idx] <= timestamp and check_lst[r_idx] > timestamp:
                
                # on left side
                if(check_lst[m_idx] > timestamp):
                    r_idx = m_idx - 1
                    m_idx = r_idx // 2
                    l_idx += 1
                # on right side
                else:
                    r_idx -= 1
                    l_idx = m_idx + 1
                    m_idx = (r_idx + l_idx) // 2
            
            return self.valmap[check_lst[r_idx]]
        # no vals to search
        else:
            return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
