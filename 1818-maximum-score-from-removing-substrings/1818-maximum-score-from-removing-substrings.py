class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # Prioritize higher scoring pair
        if x > y:
            return self.calculate_score(s, 'a', 'b', x, y)
        else:
            return self.calculate_score(s, 'b', 'a', y, x)

    def calculate_score(self, s: str, first: str, second: str, high: int, low: int) -> int:
        count_first = count_second = score = 0
        s += '!'  # Sentinel to trigger final score flush

        for char in s:
            if char == first:
                count_first += 1
            elif char == second:
                if count_first > 0:
                    # Found a valid high-value pair
                    count_first -= 1
                    score += high
                else:
                    # Not enough `first`, store `second` for later
                    count_second += 1
            else:
                # For leftover mismatched `first` and `second`, do low-value pairing
                score += low * min(count_first, count_second)
                count_first = count_second = 0

        return score
