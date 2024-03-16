class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maps = {}
        n1,n0,maxLen = 0,0,0
        maps[0] = -1
        for i in range(len(nums)):
            n1 += nums[i]
            n0 = (i+1) - n1
            if n1-n0 in maps:
                maxLen = max(maxLen, i-maps[n1-n0])
            else:
                maps[n1-n0] = i
        return maxLen
