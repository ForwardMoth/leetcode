class Solution:
    """Two pointer way"""
    def reverseWords(self, s):
        words = s.split()
        for k in range(len(words)):
            i, j = 0, len(words[k]) - 1
            words[k] = list(words[k])

            while i < j:
                words[k][i], words[k][j] = words[k][j], words[k][i]
                i += 1
                j -= 1

            words[k] = "".join(words[k])

        return " ".join(words)


s = "Let's take LeetCode contest"

solution = Solution().reverseWords(s)

print(solution)
