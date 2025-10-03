from typing import List

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        # Sort edges by cost
        connections.sort(key=lambda x: x[2])

        parent = list(range(n + 1))  # cities are 1..n
        size = [1] * (n + 1)

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # path compression (halving)
                x = parent[x]
            return x

        def union(a: int, b: int) -> bool:
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]
            return True

        used = 0
        total = 0
        for u, v, w in connections:
            if union(u, v):
                total += w
                used += 1
                if used == n - 1:
                    return total
        return -1
