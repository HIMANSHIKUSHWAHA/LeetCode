class Solution:
    def solve(self, mp):
        mini = float('inf')
        maxi = 0
        for val in mp.values():
            mini = min(mini, val)
            maxi = max(maxi, val)
        return mini == maxi

    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            mp = {}
            for j in range(i, n):
                mp[s[j]] = mp.get(s[j], 0) + 1
                if self.solve(mp):
                    l = j - i + 1
                    ans = max(ans, l)
        return ans