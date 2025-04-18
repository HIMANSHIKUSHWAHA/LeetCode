class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i]=nums[i]*nums[i]
        l=0
        r=len(nums)-1
        s=[]
        while l<=r:
            if nums[l]<nums[r]:
                s.append(nums[r])
                r-=1
            else:
                s.append(nums[l])
                l+=1
        return s[::-1]


        