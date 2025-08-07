from typing import List
from functools import lru_cache

class Solution:
    def maxCollectedFruits(self, mat: List[List[int]]) -> int:
        n = len(mat)

        # Step 1: Child 1 eats all diagonal fruits
        total = 0
        for i in range(n):
            total += mat[i][i]
            mat[i][i] = 0

        # Step 2: Child 2 (from bottom-left to top-right)
        @lru_cache(maxsize=None)
        def dfs3(row, col):
            if row < 0 or col < 0 or row >= n or col >= n:
                return 0

            val = mat[row][col]
            res = 0

            if row == col:
                res = dfs3(row + 1, col + 1)
            elif row - 1 == col:
                res = max(dfs3(row + 1, col + 1), dfs3(row, col + 1))
            else:
                res = max(
                    dfs3(row + 1, col + 1),
                    dfs3(row, col + 1),
                    dfs3(row - 1, col + 1)
                )

            return val + res

        # Step 3: Child 3 (from top-right to bottom-left)
        @lru_cache(maxsize=None)
        def dfs2(row, col):
            if row < 0 or col < 0 or row >= n or col >= n:
                return 0

            val = mat[row][col]
            res = 0

            if row == col:
                res = dfs2(row + 1, col + 1)
            elif row == col - 1:
                res = max(dfs2(row + 1, col + 1), dfs2(row + 1, col))
            else:
                res = max(
                    dfs2(row + 1, col + 1),
                    dfs2(row + 1, col),
                    dfs2(row + 1, col - 1)
                )

            return val + res

        total += dfs3(n - 1, 0)
        total += dfs2(0, n - 1)

        return total
