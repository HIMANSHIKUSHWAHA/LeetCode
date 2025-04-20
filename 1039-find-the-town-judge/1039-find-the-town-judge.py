class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        l = len(trust)

        trusts = [0 for i in range(n + 1)]
        is_trusted = [0 for i in range(n + 1)]

        for i in range(l):
            trusts[trust[i][0]] += 1
            is_trusted[trust[i][1]] += 1
        
        for i in range(1, n + 1):
            if trusts[i] == 0:
                if is_trusted[i] == n - 1:
                    return i
        return -1