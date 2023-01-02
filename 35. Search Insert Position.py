class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
        return right + 1

nums = [1, 3, 5, 6]
target = 2

solution = Solution().searchInsert(nums, target)

print(solution)


