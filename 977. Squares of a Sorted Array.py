class Solution:
    """Two pointers way"""
    def sortedSquares(self, nums):
        l, r = 0, len(nums) - 1
        k = len(nums) - 1
        res = [0] * len(nums)
        while k >= 0:
            if nums[l] ** 2 > nums[r] ** 2:
                res[k] = nums[l] ** 2
                l += 1
            else:
                res[k] = nums[r] ** 2
                r -= 1
            k -= 1
        return res


nums = [-7, -3, 2, 3, 11]

solution = Solution().sortedSquares(nums)

print(solution)