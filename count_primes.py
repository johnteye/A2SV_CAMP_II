class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        prime= [1 for i in range(n)]
        prime[0], prime[1] = 0, 0

        for i in range(2, n):
            if not prime[i]:
                continuea
            for j in range(i+i, n, i):
                if j%i == 0:
                    prime[j] = 0

        return sum(prime)
