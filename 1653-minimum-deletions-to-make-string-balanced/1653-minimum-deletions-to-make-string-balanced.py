class Solution(object):
    def minimumDeletions(self, s):
        b_count = 0
        deletions = 0

        for ch in s:
            if ch == 'b':
                b_count += 1
            else:  # ch == 'a'
                # Either delete this 'a' (deletions + 1)
                # or delete all previous 'b's (b_count)
                deletions = min(deletions + 1, b_count)

        return deletions
        """
        :type s: str
        :rtype: int
        """
        