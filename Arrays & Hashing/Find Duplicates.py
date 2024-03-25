class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dp = set()
        arr = []
        for i in range(len(nums)):
            if nums[i] in dp:
                arr.append(nums[i])
            dp.add(nums[i])
        return arr
