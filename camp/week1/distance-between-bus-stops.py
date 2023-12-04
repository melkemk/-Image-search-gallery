class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if(start==destination):
            return 0
        if(start>destination):
            start,destination=destination,start
        ans=0
        first=0
        for i in range(start):
            first+=distance[i]
        for i in range(start,destination):
            ans+=distance[i]
        for i in range(destination,len(distance)):
            first+=distance[i]
        return min(ans,first)