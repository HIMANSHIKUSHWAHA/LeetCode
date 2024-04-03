class Solution(object):
    def isAnagram(self, s, t):
        a=sorted(s)
        b=sorted(t)
        return a==b          
            


        