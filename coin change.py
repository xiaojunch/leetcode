class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        # DP solution
        MAX = amount+10
        dp = [0]*(amount+1)
                     
        for i in range(1, amount+1):
            feasible = []
            for j in coins:
                if j <= i:
                    temp_min = dp[i-j] + 1
                    feasible.append(temp_min)
            dp[i] = min(feasible) if feasible else MAX
            
        return -1 if dp[amount] >= MAX else dp[amount]
