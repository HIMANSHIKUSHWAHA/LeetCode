from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        i = 0
        curr_sum = 0
        max_sum = 0

        for j in range(len(nums)):
            count[nums[j]] += 1
            curr_sum += nums[j]

            # If window size > k, slide it
            if j - i + 1 > k:
                count[nums[i]] -= 1
                if count[nums[i]] == 0:
                    del count[nums[i]]
                curr_sum -= nums[i]
                i += 1

            # If window size == k and all elements are distinct
            if j - i + 1 == k and len(count) == k:
                max_sum = max(max_sum, curr_sum)

        return max_sum



        