class Solution:
    def pivotIndex(self, nums):
        sum = 0
        for i in nums:
            sum += i

        left_sum, right_sum = 0, sum
        for i in range(len(nums)):
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]

        return -1


nums = [2,1,-1]

solution = Solution().pivotIndex(nums)

print(solution)

