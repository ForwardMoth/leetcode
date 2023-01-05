class Solution:
    """Two pointers way"""
    def reverseString(self, s):
        l, r = 0, len(s) - 1

        while l <= r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        print(str)

        # s[:] = s[::-1]




str = ["H","a","n","n","a","h"]

Solution().reverseString(str)