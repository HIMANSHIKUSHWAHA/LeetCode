class Solution:
    def minDifference(self, n: int, k: int) -> list[int]:
        def dfs(num: int, parts: int) -> tuple:
            # Base case: only one factor left
            if parts == 1:
                return (num,)

            min_diff = float("inf")      # best difference found so far
            best_factors = None          # best factorization array

            # Try every divisor i of num
            for i in range(1, int(num**0.5) + 1):
                if num % i == 0:
                    quotient = num // i

                    # Recursively factorize quotient into (parts-1) parts
                    remaining_factors = dfs(quotient, parts - 1)

                    # Build new factorization including current divisor i
                    current_factors = (i,) + remaining_factors

                    # Sort to easily compute min and max factor
                    sorted_factors = tuple(sorted(current_factors))
                    diff = sorted_factors[-1] - sorted_factors[0]

                    # Keep track of the factorization with the minimum difference
                    if diff < min_diff:
                        min_diff = diff
                        best_factors = sorted_factors
                        #Best split found
                        if min_diff==0:
                            break

            return best_factors

        return list(dfs(n, k))