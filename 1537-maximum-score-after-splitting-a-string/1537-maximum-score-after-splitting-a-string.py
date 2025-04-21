class Solution:
    def maxScore(self, s: str) -> int:
        left=[]
        right=[]
        score=0
        left_sum, right_sum=0, 0
        for i in range(1, len(s)):
            left=s[:i]
            right=s[i:]
            left_sum = left.count('0')
            right_sum = right.count('1')
            total_score=right_sum+left_sum
            score=max(score, total_score)
        return score



# hashmap={}





        