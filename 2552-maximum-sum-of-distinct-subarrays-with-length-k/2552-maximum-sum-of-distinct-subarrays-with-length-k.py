from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        res, i, cur_sum = 0, 0, 0
        for j in range(len(nums)):
            cur_sum+=nums[j]
            count[nums[j]]+=1
            if j-i+1>k:
                cur_sum-=nums[i]
                count[nums[i]]-=1
                if count[nums[i]]==0:
                    del count[nums[i]]
                i+=1
            if len(count)==k and j-i+1==k:
                res=max(res, cur_sum)
        return res
        


        