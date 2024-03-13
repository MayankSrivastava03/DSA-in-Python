class Solution:
    def pivotInteger(self, n: int) -> int:
        rightsum = n*(n+1)//2
        index = -1
        if n==1:
            return 1
        for i in range(n):
            leftsum = i*(i+1)//2
            temp = rightsum - leftsum + i
            if temp == leftsum:
                index = i
        return index
