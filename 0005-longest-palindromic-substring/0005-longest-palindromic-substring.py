class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s)==1:
            return s
        start=0
        max_len=0
        def expand(l, r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return l+1, r-1
        for i in range(len(s)):
            l1, r1 = expand(i, i)
            l2, r2 = expand(i, i+1)
            if r1-l1+1>max_len:
                start=l1
                max_len=r1-l1+1
            if r2-l2+1>max_len:
                start=l2
                max_len=r2-l2+1
        return s[start:start+max_len]
        

        