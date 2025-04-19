class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        l, counter=0, 0
        r=n-1
        while l<r:
            if nums[l]+nums[r]<target:
                counter+=r-l
                l+=1
            else:
                r-=1
        return counter
            

        
            


        