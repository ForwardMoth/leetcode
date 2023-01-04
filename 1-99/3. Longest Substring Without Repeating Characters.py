class Solution:
    def count_check(self, s):
        return len(set(s)) != len(s)

    def lengthOfLongestSubstring(self, s):
        if len(s) < 1:
            return 0
        i, max = 0, 1
        for j in range(0, len(s)):
            if self.count_check(s[i:j+1]):
                while i < j:
                    if self.count_check(s[i:j+1]):
                        i += 1
                    else:
                        break
            else:
                if j - i + 1 > max:
                    max = j - i + 1

        return max

s = "pwwkew"

solution = Solution().lengthOfLongestSubstring(s)

print(solution)



