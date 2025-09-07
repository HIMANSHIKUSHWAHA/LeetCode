from typing import List
import math
class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        # max_r = max(r for _, r in queries)
        # f=[0]*(max_r+1)
        # for x in range(1, max_r+1):
        #     f[x]=1+f[x//4]
        # pref=[0]*(max_r+1)
        # for x in range(1, max_r+1):
        #     pref[x]=pref[x-1]+f[x]
        # ans=0
        # for l, r in queries:
        #     total=pref[r]-pref[l-1]
        #     ans += (total+1)//2
        # return ans
        def prefix_sum(n: int)-> int:
            if n==0:
                return 0
            res, k, base=0,0,1
            while base * 4 <=n:
                res += (k+1) * (3*base)
                base *= 4
                k +=1
            res += (k+1) * (n-base+1)
            return res
        ans =0
        for l, r in queries:
            total = prefix_sum(r) - prefix_sum(l-1)
            ans += (total+1)//2
        return ans
        