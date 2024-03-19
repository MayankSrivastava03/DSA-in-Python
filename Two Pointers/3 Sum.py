res = []
class Solution:
    def twoSum(self, nums: List[int], target:int, i:int, j:int) -> List[int]:
        while i<j:
            if nums[i] + nums[j] > target:
                j-=1
            elif nums[i] + nums[j] < target:
                i+=1
            else:
                while i<j and nums[i] == nums[i+1]:
                    i+=1
                while i<j and nums[j] == nums[j-1]:
                    j-=1
                res.append([-target,nums[i],nums[j]])
                i+=1
                j-=1
            
            
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res.clear()
        if len(nums)<3:
            return
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            n1 = nums[i]
            target = -n1

            self.twoSum(nums, target, i+1, len(nums)-1)
        return res
           
