# from itertools import cycle
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        s=[0]*n
        for i in range(n):
            if k>0:
                for j in range(i+1, i+1+k):
                    s[i]+=code[j%n]
            elif k<0:
                for j in range(i-1, i-1-abs(k), -1):
                    s[i]+=code[j%n]
            else: 
                s[i]=0
        return s
            


            



        