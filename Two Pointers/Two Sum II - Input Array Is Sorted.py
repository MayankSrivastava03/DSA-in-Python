class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(numbers)):
            remaining = target - numbers[i]
            if remaining in hashMap:
                return [hashMap[remaining], i+1]
            hashMap[numbers[i]] = i+1
        return
