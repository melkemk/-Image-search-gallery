class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if(len(nums)==1): return True
        def is_non_decreasing(lst):
            return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

        # Check the first modification
        tempnum = nums.copy()
        tempnum[0] = tempnum[1] - 1
        if is_non_decreasing(tempnum):
            return True

        # Check the second modification
        tempnum = nums.copy()
        tempnum[len(nums) - 1] = tempnum[len(nums) - 2] + 1
        if is_non_decreasing(tempnum):
            return True

        # Check modifications in the middle
        for i in range(1, len(nums) - 1):
            tempnum = nums.copy()
            tempnum[i] = (tempnum[i - 1] + tempnum[i + 1]) // 2

            if is_non_decreasing(tempnum):
                return True

        return False
