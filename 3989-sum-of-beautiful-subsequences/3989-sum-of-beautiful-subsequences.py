from collections import defaultdict

M_val = 70000

class Solution:
    precomputed = False
    phi_g = None
    divisors_g = None

    def totalBeauty(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        M = M_val
        if not Solution.precomputed:
            phi = list(range(M + 1))
            for i in range(2, M + 1):
                if phi[i] == i:
                    for j in range(i, M + 1, i):
                        phi[j] -= phi[j] // i
            Solution.phi_g = phi

            divisors = [[] for _ in range(M + 1)]
            for i in range(1, M + 1):
                for j in range(i, M + 1, i):
                    divisors[j].append(i)
            Solution.divisors_g = divisors
            Solution.precomputed = True

        phi_arr = Solution.phi_g
        divisors_arr = Solution.divisors_g

        arr_by_d = defaultdict(list)
        divisors_appear = set()
        for x in nums:
            for d in divisors_arr[x]:
                if d <= M:
                    arr_by_d[d].append(x)
                    divisors_appear.add(d)
        
        ans = 0
        for d in divisors_appear:
            L = arr_by_d[d]
            if not L:
                continue
            distinct_vals = sorted(set(L))
            comp = {val: idx + 1 for idx, val in enumerate(distinct_vals)}
            n_comp = len(distinct_vals)
            fenw = [0] * (n_comp + 1)
            total_count = 0
            for x in L:
                pos = comp[x]
                s = 0
                idx = pos - 1
                while idx > 0:
                    s = (s + fenw[idx]) % mod
                    idx -= idx & -idx
                count_here = (1 + s) % mod
                total_count = (total_count + count_here) % mod
                idx = pos
                while idx <= n_comp:
                    fenw[idx] = (fenw[idx] + count_here) % mod
                    idx += idx & -idx
            ans = (ans + phi_arr[d] * total_count) % mod
        return ans % mod