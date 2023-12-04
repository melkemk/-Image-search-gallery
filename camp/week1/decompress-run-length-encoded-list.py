class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        a=[]
        i=0
        while(i<len(nums)-1):
            for j in range(nums[i]):
                a.append(nums[i+1])
            i+=2
        return a