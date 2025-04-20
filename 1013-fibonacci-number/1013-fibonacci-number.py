class Solution:
    def fib(self, n: int) -> int:
        #TOP-DOWN APPROACH
        # memo={0:0, 1:1}
        # def f(x):
        #     if x in memo:
        #         return memo[x]
        #     else:
        #         memo[x]=f(x-1)+f(x-2)
        #         memo[x]
        #         return memo[x]
        # return f(n)

        #bottom up approach
        if n==0:
            return 0
        if n==1:
            return 1
        # d=[0]*(n+1)
        # d[0]=0
        # d[1]=1
        # for i in range(2, n+1):
        #     d[i]=d[i-1]+d[i-2]
        # return d[n]
        
        prev=0
        curr=1
        for i in range(2, n+1):
            prev, curr = curr, prev+curr
        return curr