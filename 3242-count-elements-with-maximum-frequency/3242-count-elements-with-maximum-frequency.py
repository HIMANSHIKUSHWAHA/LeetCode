class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        x = Counter(nums)
        a = max(x.values())
        y = [num for num, freq in x.items() if freq == a]
        c = a * len(y)
        return c