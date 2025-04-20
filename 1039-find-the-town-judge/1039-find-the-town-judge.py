from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d = defaultdict(list)
        trusted=[0] * (n + 1)
        for u, v in trust:
            d[u].append(v)
            trusted[v]+=1
        for i in range(1, n+1):
            if i not in d and trusted[i]==n-1:
                return i
        return -1
        


        