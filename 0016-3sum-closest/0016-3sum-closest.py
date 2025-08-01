class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum=float('inf')
        for i in range(len(nums)-2):
            l, r =i+1, len(nums)-1
            while l<r:
                curr_sum=nums[i]+nums[l]+nums[r]
                if abs(curr_sum-target) < abs(closest_sum-target):
                    closest_sum=curr_sum
                if curr_sum<target:
                    l+=1
                elif curr_sum>target:
                    r-=1
                else:
                    return target
        return closest_sum

        
        