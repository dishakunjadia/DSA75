class Solution(object):
    def countCharacters(self, words, chars):
        chars_count = Counter(chars)
        total = 0


        for s in words:
            word_count = Counter(s)
            if all(word_count[c] <= chars_count[c] for c in word_count):
                total += len(s)

        return total
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        