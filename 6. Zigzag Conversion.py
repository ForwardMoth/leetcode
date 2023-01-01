class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        new_s = ""
        for i in range(numRows):
            j = i
            while j < len(s):
                new_s += s[j]
                if i != 0 and i != numRows - 1:
                    new_s += s[j + (numRows - 1 - i) * 2] if j + (numRows - 1 - i) * 2 < len(s) else ""
                j += (numRows - 1) * 2

        return new_s


s = "A"
n = 1

solution = Solution().convert(s, n)


print(solution)
