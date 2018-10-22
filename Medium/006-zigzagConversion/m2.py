class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        index, step = 0, 1
        l = [""] * numRows

        for item in s:
            l[index] += item
            if index == 0:
                step = 1
            if index == numRows - 1:
                step = -1
            index += step

        return "".join(l)