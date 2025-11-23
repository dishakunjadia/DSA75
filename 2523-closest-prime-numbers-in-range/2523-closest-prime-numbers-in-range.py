class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if right < 2:
            return [-1, -1]
        
        # Step 1: Sieve up to right
        sieve = [True] * (right + 1)
        sieve[0] = sieve[1] = False
        
        p = 2
        while p * p <= right:
            if sieve[p]:
                for i in range(p*p, right + 1, p):
                    sieve[i] = False
            p += 1
        
        # Step 2: Collect primes in [left, right]
        primes = [i for i in range(left, right + 1) if sieve[i]]
        
        if len(primes) < 2:
            return [-1, -1]
        
        # Step 3: Find closest pair
        best_pair = [-1, -1]
        min_diff = float('inf')
        
        for i in range(1, len(primes)):
            diff = primes[i] - primes[i - 1]
            if diff < min_diff:
                min_diff = diff
                best_pair = [primes[i - 1], primes[i]]
        
        return best_pair