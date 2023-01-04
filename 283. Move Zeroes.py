class Solution:
    def moveZeroes(self, nums):
        l = 0
        res = [0] * len(nums)
        for r in range(len(nums)):
            if nums[r] != 0:
                res[l] = nums[r]
                l += 1
        nums[:] = res

        print(nums)

