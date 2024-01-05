class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)

        res = [False] * n
        greatestCandy = max(candies)
        
        for i in range(0, n):
            if candies[i] + extraCandies >= greatestCandy:
                res[i] = True
        
        return res