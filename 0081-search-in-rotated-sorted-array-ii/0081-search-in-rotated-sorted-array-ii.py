from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        s = []

        # Handle case where array is not rotated
        pivot = 0
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                pivot = i + 1
                s.extend(nums[pivot:])    # from pivot to end
                s.extend(nums[:pivot])    # from start to pivot
        if not s:
            s = nums[:]
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if s[m] == target:
                return True
            elif s[m] < target:
                l = m + 1
            else:
                r = m - 1

        return False

        