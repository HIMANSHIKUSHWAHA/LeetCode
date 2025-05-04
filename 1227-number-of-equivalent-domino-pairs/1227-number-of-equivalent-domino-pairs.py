class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        arr=[0]*100
        ret = 0
        for a, b in dominoes:
            val= 10*a+b if a<=b else 10*b+a
            ret+=arr[val]
            arr[val]+=1
        return ret

        