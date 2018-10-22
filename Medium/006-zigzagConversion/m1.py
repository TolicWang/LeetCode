class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        k = 2 * numRows - 2
        lens = len(s)
        if lens <= numRows or k == 0:
            return s
        indices = []
        for line, i in enumerate(range(k, -1, -2)):
            index = line#  0    1   2   3   4
            indices.append(index)
            space = i # 6 4 2
            if (line == 0 or line == numRows - 1):
                while (index + k < lens):
                    index += k
                    indices.append(index)
            else:
                while (index + space < lens):
                    index += space
                    space = k - space
                    indices.append(index)
        conversion = ""
        for j in indices:
            conversion+=s[j]
        # print(indices)
        return conversion



print(Solution().convert('ABC',2))

