class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mapit = defaultdict(list)
        for word in strs:
            sorted_words = ''.join(sorted(word))
            mapit[sorted_words].append(word)
        return list(mapit.values())   
        
        
