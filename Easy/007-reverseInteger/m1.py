class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        str_x = str(x)
        list_x = list(str_x)
        sign = 1
        if x < 0:
            sign = -1
            list_x.remove('-')
        list_x.reverse()
        num = ""
        for item in list_x:
            num += item
        num = int(num)*sign
        if num < -2147483648 or num > 2147483647:
            return 0
        return num


print(Solution().reverse(-1231234))
