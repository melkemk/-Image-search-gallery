class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            if(nums[i]+nums[i+1]>nums[i+2] and nums[1+i]+nums[i+2]>nums[i] and nums[i]+nums[i+2]>nums[i+1]):
                return  nums[i]+nums[i+2]+nums[i+1]
        return 0