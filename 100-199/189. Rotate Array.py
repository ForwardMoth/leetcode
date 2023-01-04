class Solution:
    def rotate(self, nums, k):
        if k > len(nums):
            k = k % len(nums)

        nums = nums[len(nums)-k:] + nums[:len(nums)-k]

        print(nums)


nums = [-1,-100,3,99]

k = 2

Solution().rotate(nums, k)
