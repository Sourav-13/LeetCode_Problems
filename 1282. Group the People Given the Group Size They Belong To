class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res = {}
        for i, val in enumerate(groupSizes):
            res.setdefault(val, []).append(i)
            
        ans = []
        for x in res:
            for i in range(0, len(res[x]), x):
                ans.append(res[x][i:i + x])
        return ans
    
    
    
# better
from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result = []
        group_idx = defaultdict(list)

        for i in range(len(groupSizes)):
            group_idx[groupSizes[i]].append(i)

            if len(group_idx[groupSizes[i]]) == groupSizes[i]:
                result.append(list(group_idx[groupSizes[i]]))
                group_idx[groupSizes[i]].clear()
        
        return result



class Solution:
    def groupThePeople(self, groupSizes):
        ht = defaultdict(list)
        res = []

        for i, size in enumerate(groupSizes):
            ht[size].append(i)
            if len(ht[size]) == size:
                res.append(ht[size][:])
                ht[size] = []  # Replace .clear() with reassigning an empty list

        return res

        