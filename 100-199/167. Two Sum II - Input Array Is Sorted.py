class Solution:
    def two_sum(self, numbers, target):
        l = 0

        for r in range(len(numbers)-1, -1, -1):
            while numbers[l] + numbers[r] < target:
                l += 1

            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]


numbers = [5, 25, 75]

target = 100

solution = Solution().two_sum(numbers, target)

print(solution)