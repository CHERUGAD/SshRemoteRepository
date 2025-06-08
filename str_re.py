class Solution(object):
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right :
            s[left], s[right] = s[right], s[left]
            left += 1
            right -=1

sol = Solution()
lists = [
    ["h", "e", "l", "l", "o"],
    ["H", "a", "n", "n", "a", "h"]
]

for lst in lists:
    sol.reverseString(lst)
    print(lst)
