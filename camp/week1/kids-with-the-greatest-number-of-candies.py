class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[]
        maximum=max(candies)-extraCandies
        for i in candies:
            if(i>=maximum):
                ans.append(True)
                continue
            ans.append(False)
        return ans
