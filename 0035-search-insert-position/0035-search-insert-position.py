class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        l=0
        r=n-1
        if target in nums:
            while l<=r:
                m=(l+r)//2
                if nums[m]==target:
                    return m
                elif nums[m]<target:
                    l=m+1
                elif nums[m]>target:
                    r=m-1
        else:
            if target > nums[-1]:
                return n
            elif target < nums[0]:
                return 0
            else:
                for i in range(n):
                    if nums[i]< target and nums[i+1]> target:
                        return i+1
                
            
            
        