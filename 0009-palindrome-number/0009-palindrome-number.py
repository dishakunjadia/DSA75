class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
    
        # Numbers ending with 0 (but not 0 itself) cannot be palindrome
        if x % 10 == 0 and x != 0:
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # For odd digit count, we remove the middle digit using // 10
        return x == reversed_half or x == reversed_half // 10