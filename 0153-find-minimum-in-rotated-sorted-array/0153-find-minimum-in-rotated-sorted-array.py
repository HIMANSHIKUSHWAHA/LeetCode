from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # If mid element is greater than the rightmost,
            # the min must be in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid  # min is at mid or to the left

        return nums[left]
