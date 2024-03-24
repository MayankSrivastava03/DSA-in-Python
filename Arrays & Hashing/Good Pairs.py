class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dp = {}
        c = 0
        for num in nums:
            if num in dp:
                c += dp[num]
                dp[num] += 1
            else:
                dp[num] = 1
        return c
