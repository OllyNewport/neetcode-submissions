class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def checker(piles, k):
            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k
            return hours

        answer = max(piles)

        while l <= r:
            k = (l + r) // 2
            hours = checker(piles, k)

            if hours <= h:
                answer = k
                r = k - 1
            else:
                l = k + 1

        return answer