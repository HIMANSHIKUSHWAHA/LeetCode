from collections import defaultdict
from typing import List
class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:

        pairs_by_r = defaultdict(list)
        for a, b in conflictingPairs:
            u, v = (a, b) if a < b else (b, a)
            pairs_by_r[v].append(u)

        # 2. Compute for each r:
        #    M1[r]: highest u+1, M2[r]: second highest u+1, cnt1[r]: count of M1[r]
        M1 = [0] * (n + 2)
        M2 = [0] * (n + 2)
        cnt1 = [0] * (n + 2)
        for r, us in pairs_by_r.items():
            first = second = 0
            count_first = 0
            for u in us:
                val = u + 1
                if val > first:
                    second = first
                    first = val
                    count_first = 1
                elif val == first:
                    count_first += 1
                elif val > second:
                    second = val
            M1[r], M2[r], cnt1[r] = first, second, count_first

        # 3. Build the original barrier array and compute total_valid
        #    barrier_orig[r] = max barrier up to r
        barrier_orig = [0] * (n + 1)
        barrier = 1
        total_valid = 0
        for r in range(1, n + 1):
            # barrier at r is max of previous barrier and M1[r]
            barrier = max(barrier, M1[r])
            barrier_orig[r] = barrier
            # valid subarrays ending at r count = r - barrier + 1
            total_valid += (r - barrier + 1)

        # 4. Identify events: positions where barrier_orig strictly increases
        events = []
        for r in range(1, n + 1):
            if r == 1 or barrier_orig[r] > barrier_orig[r - 1]:
                events.append((r, barrier_orig[r]))

        # 5. For each event, simulate removing its unique max‑conflict pair
        best_delta = 0
        k = len(events)
        for idx, (pos, old_barrier) in enumerate(events):
            prev_barrier = 1 if idx == 0 else events[idx - 1][1]
            new_barrier = max(prev_barrier, M2[pos])
            # only if there is a unique drop
            if cnt1[pos] == 1 and new_barrier < old_barrier:
                # segment of effect: [pos … r_end]
                r_end = events[idx + 1][0] - 1 if idx + 1 < k else n

                # simulate the barrier under removal
                barrier_removal = new_barrier
                delta = 0
                for r in range(pos, r_end + 1):
                    # at each r, barrier_removal = max(previous, M1[r])
                    if r > pos:
                        barrier_removal = max(barrier_removal, M1[r])
                    # gain is how much original barrier was higher
                    delta += (barrier_orig[r] - barrier_removal)
                best_delta = max(best_delta, delta)

        return total_valid + best_delta
        