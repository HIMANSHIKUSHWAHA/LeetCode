class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen, complement={}, 0
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in seen:
                return [seen[complement], i+1]
            seen[numbers[i]]=i+1
        