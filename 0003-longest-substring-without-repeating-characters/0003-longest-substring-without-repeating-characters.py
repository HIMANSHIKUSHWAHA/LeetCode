class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, longest =0, 0
        keep=set()
        for i in range(len(s)):
            while s[i] in keep:
                keep.remove(s[l])
                l+=1
            w=i-l+1
            longest=max(w, longest)
            keep.add(s[i])
        return longest
        


                
        