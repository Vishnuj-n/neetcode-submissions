class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mk = max(piles)
        l = 1                  # speed cannot be 0
        hi = mk

        def sum_1(k, array):
            count = 0
            for i in array:
                count += (i + k - 1) // k
            return count

        ans = mk
        while l <= hi:
            mid = (l + hi) // 2
            s1 = sum_1(mid, piles)

            if s1 <= h:
                ans = mid      # possible answer
                hi = mid - 1
            else:
                l = mid + 1

        return ans



        

        