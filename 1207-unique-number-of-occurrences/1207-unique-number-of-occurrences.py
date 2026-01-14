class Solution(object):
    def uniqueOccurrences(self, arr):

        freq = {}
        for num in arr: 
            freq[num] = freq.get(num, 0) + 1 
        return len(freq.values()) == len(set(freq.values()))
        """
        :type arr: List[int]
        :rtype: bool
        """
        