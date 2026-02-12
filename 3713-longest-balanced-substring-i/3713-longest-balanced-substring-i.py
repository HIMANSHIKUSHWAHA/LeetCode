class Solution:
    def longestBalanced(self, s: str) -> int:
        s = s + "_"
        N = len(s)

        def f(s):
            alpha = list(set(s))
            pairs = [(a, b) for i, a in enumerate(alpha[:-1]) for b in alpha[i+1:]]
            beg = defaultdict(list)
            end = defaultdict(list)
            for a, b in pairs:
                beg[a].append((a,b))
                end[b].append((a,b))
            balances = { pair: 0 for pair in pairs }
            pairs_s0 = beg[alpha[0]]
            init = tuple(balances[p] for p in pairs_s0)
            seen = {}
            seen[init] = -1
            best = 0
            for i, c in enumerate(s):
                for a in beg[c]:
                    balances[a] += 1
                for b in end[c]:
                    balances[b] -= 1
                key = tuple(balances[p] for p in pairs_s0)
                if key in seen:
                    best = max(best, i - seen[key])
                else:
                    seen[key] = i
            return best

        def split(sz):
            counts = defaultdict(int)
            subs = set()
            l, r = 0, 0
            while r < N:
                while r < N and len(counts) <= sz:
                    counts[s[r]] += 1
                    r += 1
                subs.add(s[l:r-1])
                while l < r and len(counts) > sz:
                    counts[s[l]] -= 1
                    if counts[s[l]] == 0: del counts[s[l]]
                    l += 1
            return list(subs)

        ws = []
        uniq = set(s)
        for sz in range(1, len(uniq)):
            w = split(sz)
            ws.extend(w)
        return max(f(s) for s in ws)