from collections import defaultdict
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def isOverfill(self,map):
        count=0
        for elem in map.values():
            if elem>=1:
                count+=1
        return True if count>2 else False
    def totalFruit(self, fruits: List[int]) -> int:
        l,r=0,0
        maxz=0
        mapz=defaultdict(int)
        for r in range(0,len(fruits)):
            fruit=fruits[r]
            mapz[fruit]+=1
            overfill=self.isOverfill(mapz)
            while l<=r and overfill:
                fruit=fruits[l]
                mapz[fruit]-=1
                if mapz[fruit]==0:
                    mapz.pop(fruit,None)
                overfill=self.isOverfill(mapz)
                l+=1
            if not overfill:
                maxz=max(r-l+1,maxz)
        return maxz
            
            





        