class Solution:
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums


nums = [3,1,2,10,1]

solution = Solution().runningSum(nums)

print(solution)
