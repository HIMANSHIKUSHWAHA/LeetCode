import heapq

class Solution(object):
    def trapRainWater(self, heightMap):
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        pq = []

        for i in range(m):
            for j in [0, n - 1]:
                heapq.heappush(pq, (heightMap[i][j], i, j))
                visited[i][j] = True

        for j in range(n):
            for i in [0, m - 1]:
                if not visited[i][j]:
                    heapq.heappush(pq, (heightMap[i][j], i, j))
                    visited[i][j] = True

        ans = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while pq:
            h, x, y = heapq.heappop(pq)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    ans += max(0, h - heightMap[nx][ny])
                    heapq.heappush(pq, (max(h, heightMap[nx][ny]), nx, ny))

        return ans