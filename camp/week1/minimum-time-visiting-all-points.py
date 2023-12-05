class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total=0
        for i in range(len(points)-1):
            point=points[i]
            while(point[0]!=points[i+1][0] and (point[1]!=points[i+1][1]  )):
                if(point[0]>points[i+1][0]):
                    point[0]-=1
                else:
                    point[0]+=1
                if(point[1]>points[i+1][1]):
                    point[1]-=1
                else:
                    point[1]+=1
                total+=1
            while(point[0]!=points[i+1][0]):
                if(point[0]>points[i+1][0]):
                    point[0]-=1
                else:
                    point[0]+=1
                total+=1
            while (point[1]!=points[i+1][1]  ):
                if(point[1]>points[i+1][1]):
                    point[1]-=1
                else:
                    point[1]+=1
                total+=1
        return total