class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7

        seats = [i for i, c in enumerate(corridor) if c == 'S']
        total_seats = len(seats)

        if total_seats == 0 or total_seats % 2 != 0:
            return 0

        ways = 1

        for i in range(2, total_seats, 2):
            gap = seats[i] - seats[i - 1]
            ways = (ways * gap) % MOD

        return ways