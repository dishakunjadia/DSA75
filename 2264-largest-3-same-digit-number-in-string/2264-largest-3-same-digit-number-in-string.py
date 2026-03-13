class Solution(object):
    def largestGoodInteger(self, num):
        result = ""
        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:
                result = max(result, num[i:i+3])
        return result


        """
        :type num: str
        :rtype: str
        """
        