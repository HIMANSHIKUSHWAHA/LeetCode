class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        s = set(nums)
        if s==nums:
            return 0
        i, count=0,0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    product = 0
                    product = i*j
                    if product % k == 0:
                        count+=1
        return count
                

                

        