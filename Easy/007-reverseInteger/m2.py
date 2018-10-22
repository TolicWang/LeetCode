class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            y = int('-'+str(x)[:0:-1])
        elif x > 0:
            y = int(str(x)[::-1])
        else :
            y = 0
        return y if (-(2**31))<y<((2**31)-1) else 0

