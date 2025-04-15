class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i in range(len(nums)):
            hashmap[nums[i]]=i
        for i in range(len(nums)):
            c = target - nums[i]
            if c in hashmap and hashmap[c]!=i:
                return [i, hashmap[c]]
        return []
        
            
        