class Solution:
    def create_hash(self, s):
        dict_s = {}
        for c in s:
            if c not in dict_s.keys():
                dict_s[c] = 1
            else:
                dict_s[c] += 1
        return dict_s

    def checkInclusion(self, s1, s2):
        dict_s1 = self.create_hash(s1)

        for i in range(len(s2) - len(s1) + 1):
            dict_s2 = self.create_hash(s2[i:i + len(s1)])

            if set(dict_s1.keys()) == set(dict_s2.keys()):
                k = 0
                for key in dict_s1.keys():
                    if dict_s1[key] == dict_s2[key]:
                        k += 1
                    else:
                        break

                if k == len(dict_s1):
                    return True

        return False


s1 = "ab"
s2 = "eidboaoo"

solution = Solution().checkInclusion(s1, s2)

print(solution)
