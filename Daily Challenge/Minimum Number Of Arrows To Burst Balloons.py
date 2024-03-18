class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n       = len(points)
        points.sort()
        prev    = points[0]
        count   = 1
        for i in range(1,n):
            currStartPoint = points[i][0]
            currEndPoint   = points[i][1]

            prevStartPoint = prev[0]
            prevEndPoint   = prev[1]

            if currStartPoint > prevEndPoint: # No Overlapping
                count += 1
                prev   = points[i]
            else:
                prev[0] = max(currStartPoint, prevStartPoint)
                prev[1] = min(currEndPoint, prevEndPoint)
        return count
