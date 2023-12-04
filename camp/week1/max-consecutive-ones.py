class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum=0
        temp=0
        for i in nums:
            if i ==0:
                maximum=max(maximum,temp)
                temp=0
                continue
            temp+=1
        return max(maximum,temp)