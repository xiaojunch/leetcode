class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        
        # DP solution
        N = len(coins)
        coins = [0] + coins     # extra 0 at location 0 to make indexing easier
        dp = [1] + [0]*amount   # dp[0] should be 1
        
        for i in range(1,N+1):
            for v in range(coins[i],amount+1): 
                dp[v] += dp[v-coins[i]]               
                    
        return dp[amount]
