class Solution:
    def longestPalindrome(self,s):
        def isPalindrome(s):
            length = len(s)
            if length == 1:
                return True
            if length % 2 == 0:
                middle_index = length // 2
                for i in range(middle_index):
                    if s[middle_index + i] != s[middle_index - i - 1]:
                        return False
                return True
            else:
                middle_index = length // 2
                for i in range(middle_index + 1):
                    if s[middle_index + i] != s[middle_index - i]:
                        return False
                return True
        length = len(s)
        if length == 0:
            return ""
        for i in range(length):
            sub_len = length - i
            for j in range(length-sub_len+1):
                sub_str = s[j:j+sub_len]
                if isPalindrome(sub_str):
                    return sub_str

if __name__ == '__main__':
    print(Solution().longestPalindrome('aaa'))





