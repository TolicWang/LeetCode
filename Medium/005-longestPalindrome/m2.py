class Solution:
    def longestPalindrome(self, s):
        length = len(s)
        if length < 2:
            return s# 特殊情况

        longest_pal = s[0]
        longest_pal_len = 1
        indices = 2 * length - 1
        for middle in range(indices):
            if middle == 0 or middle == indices - 1:
                continue
            else:
                if middle % 2 == 1:
                    start = (middle - 1) // 2
                    end = (middle + 1) // 2
                else:
                    start = (middle - 2) // 2
                    end = (middle + 2) // 2
                while (start >= -1 or end <= length):
                    if (start == -1 or end == length or s[start] != s[end]):
                        if len(s[start + 1:end]) > longest_pal_len:
                            longest_pal = s[start + 1:end]
                            longest_pal_len = len(s[start + 1:end])
                        break
                    start -= 1
                    end += 1
        return longest_pal


print(Solution().longestPalindrome('cccccc'))
