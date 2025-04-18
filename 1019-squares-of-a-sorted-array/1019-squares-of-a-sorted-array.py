class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # for i in range(len(nums)):
        #     nums[i]=nums[i]*nums[i]
        l=0
        r=len(nums)-1
        s=[]
        while l<=r:
            if abs(nums[l])<abs(nums[r]):
                s.append(nums[r]**2)
                r-=1
            else:
                s.append(nums[l]**2)
                l+=1
        return s[::-1]


        