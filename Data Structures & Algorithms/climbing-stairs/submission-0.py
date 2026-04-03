class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n + 1) # Initialize list
        return self.climbStairsRec(n, memo)

    # Memoization implementation
    def climbStairsRec(self, n: int, memo):
        if n == 1 or n == 0:
            return 1

        # We have computed the subtree 
        if memo[n] != -1:
            return memo[n]
        
        memo[n] = self.climbStairsRec(n - 1, memo) + self.climbStairsRec(n - 2, memo)
        return memo[n]