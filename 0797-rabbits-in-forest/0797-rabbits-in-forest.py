import math

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        hashmap={}
        total=0
        for ans in answers:
            hashmap[ans]=hashmap.get(ans, 0)+1
        for x in hashmap:
            freq=hashmap[x]
            group_size=x+1
            group=math.ceil(freq/group_size)
            total+=group*group_size
        return total




        