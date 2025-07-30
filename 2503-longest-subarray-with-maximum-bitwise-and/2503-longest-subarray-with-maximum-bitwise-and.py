class Solution:
    def longestSubarray(self, nums):
        max_val = max(nums)
        max_len = cur = 0
        for num in nums:
            if num == max_val:
                cur += 1
                max_len = max(max_len, cur)
            else:
                cur = 0
        return max_len
