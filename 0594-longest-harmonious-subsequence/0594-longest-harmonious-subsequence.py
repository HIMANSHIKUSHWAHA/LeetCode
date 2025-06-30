class Solution:
    def findLHS(self, nums: list[int]) -> int:
        from collections import Counter
        count = Counter(nums)
        max_length = 0
        
        for num in count:
            if num + 1 in count:
                max_length = max(max_length, count[num] + count[num + 1])
                
        return max_length