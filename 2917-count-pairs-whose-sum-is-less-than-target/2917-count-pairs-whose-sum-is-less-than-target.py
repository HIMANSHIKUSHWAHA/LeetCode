class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        i, counter=0, 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]<target:
                    counter+=1
        return counter
            


        