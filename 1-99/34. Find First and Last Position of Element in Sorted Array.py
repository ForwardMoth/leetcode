class Solution:
    def left_range(self, nums, target):
        l, r = 0, len(nums) - 1
        pos = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                pos = mid
                r = mid - 1

        return pos

    def right_range(self, nums, target):
        l, r = 0, len(nums) - 1
        pos = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                pos = mid
                l = mid + 1

        return pos

    def searchRange(self, nums, target):
        left = self.left_range(nums, target)
        right = self.right_range(nums, target)

        return [left, right]


nums = []
target = 0

solution = Solution().searchRange(nums,target)

print(solution)