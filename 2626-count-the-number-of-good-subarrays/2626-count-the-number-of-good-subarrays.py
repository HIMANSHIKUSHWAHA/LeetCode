class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n=len(nums)
        i=0
        freq=defaultdict(int)
        res=0
        count=0
        for j in range(n):
            num=nums[j]
            count+=freq[num]
            freq[num]+=1
            while count>=k:
                res+=n-j
                freq[nums[i]]-=1
                count-=freq[nums[i]]
                i+=1
        return res

        
               