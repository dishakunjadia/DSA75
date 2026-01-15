class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        mag_freq = {}
        for ch in magazine: 
            mag_freq[ch] = mag_freq.get(ch,0) + 1
        for ch in ransomNote:
            if mag_freq.get(ch,0) == 0:
                return False
            mag_freq[ch] -= 1 
        return True

        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        