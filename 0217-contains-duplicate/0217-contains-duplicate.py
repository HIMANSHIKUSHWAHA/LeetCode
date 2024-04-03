class Solution:
    def containsDuplicate(self, nums):
        a=set()
        for n in nums:
            if n in a:
                return True
            a.add(n)
        return False 