class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def sumsToTarget(value, target):
            return any(value + c == target for c in coins)

        dp = [-1] * (amount + 1)

        dp[0] = 0
        
        for i in range(1, amount + 1):
            dp[i] = 1 + min((dp[i-c] for c in coins if (i-c >= 0 and dp[i-c] >= 0)), default = -2) 

        res = min(dp)

        return dp[amount]
            
            