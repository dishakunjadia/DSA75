class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)

        r1 = []
        r2 = []

        for x in nums: 
            if x % 3 == 1:
                r1.append(x)
            elif x % 3 == 2: 
                r2.append(x)

        r1.sort() 
        r2.sort()

        if total % 3 == 0:
            return total 
        ans = 0

        if total % 3 == 1: 
            option1 = total - r1[0] if len(r1) >= 1 else float('-inf')
            option2 = total - (r2[0] + r2[1]) if len(r2)>=2 else float('-inf')
            ans = max(option1, option2)
        else: 
            option1 = total - r2[0] if len(r2) >= 1 else float('-inf')
            option2 = total - (r1[0] + r1[1]) if len(r1)>= 2 else float('-inf')
            ans = max(option1, option2)

        return ans