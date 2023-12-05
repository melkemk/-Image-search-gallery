class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        size=capacity
        ans=0
        for i,plant in enumerate(plants):
            if(plant<=capacity):
                capacity-=plant
                ans+=1
                if(i+1<len(plants) and capacity<plants[i+1]):
                    capacity=size
                    ans=ans+(i+1)*2
        return ans