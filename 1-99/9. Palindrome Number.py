class Solution:
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]


x = 123

solution = Solution().isPalindrome(x)

print(solution)

