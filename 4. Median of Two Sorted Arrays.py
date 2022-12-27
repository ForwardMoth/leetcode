class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        length = len(nums1)

        if length % 2 != 0:
            return nums1[length // 2]
        else:
            return (nums1[length // 2] + nums1[length // 2 - 1]) / 2

a1 = [1, 3]

a2 = [2]

solution = Solution().findMedianSortedArrays(a1, a2)

print(solution)
