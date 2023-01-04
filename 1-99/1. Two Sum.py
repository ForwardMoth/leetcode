class Solution:
    def two_sum(self, nums, target):
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


nums = [3, 2, 4]

target = 6

solution = Solution().two_sum(nums, target)

print(solution)
