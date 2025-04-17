class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        s = []
        pivot = 0
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                pivot = i + 1
                s.extend(nums[pivot:])    
                s.extend(nums[:pivot])    
        if not s:
            s = nums[:]
        # l, r = 0, n - 1
        # while l <= r:
        #     m = (l + r) // 2
        #     if s[m] == target:
        #         return True
        #     elif s[m] < target:
        #         l = m + 1
        #     else:
        #         r = m - 1

        return s[0]
        