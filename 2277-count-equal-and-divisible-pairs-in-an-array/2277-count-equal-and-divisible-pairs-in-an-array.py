from collections import defaultdict

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        pos_map = defaultdict(list)
        
        # Store positions of each number
        for idx, val in enumerate(nums):
            pos_map[val].append(idx)
        
        count = 0
        
        for indices in pos_map.values():
            for i in range(len(indices)):
                for j in range(i + 1, len(indices)):
                    if (indices[i] * indices[j]) % k == 0:
                        count += 1
                        
        return count
