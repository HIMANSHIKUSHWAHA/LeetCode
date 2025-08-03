from bisect import bisect_left, bisect_right

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        pos = [f[0] for f in fruits]
        pre = [0]
        for _, amt in fruits:
            pre.append(pre[-1] + amt)

        def get_sum(l, r):
            # Return sum of fruits from position l to r inclusive
            left = bisect_left(pos, l)
            right = bisect_right(pos, r)
            return pre[right] - pre[left]

        res = 0
        # Try going left first, then right
        for x in range(k + 1):
            left = startPos - x
            right = startPos + max(k - 2 * x, 0)
            res = max(res, get_sum(left, right))

        # Try going right first, then left
        for x in range(k + 1):
            right = startPos + x
            left = startPos - max(k - 2 * x, 0)
            res = max(res, get_sum(left, right))

        return res
