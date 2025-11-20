class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:(x[1], -x[0]))
        nums = []

        for s, e in intervals: 
            if len(nums) >= 2:
                p1 = nums[-1]
                p2 = nums[-2]
            else:
                p1=p2 =-1

            count = (s <= p1 <= e) + (s<= p2 <= e)

            if count ==2:
                continue
            elif count == 1:
                nums.append(e)
            else: 
                nums.append(e-1)
                nums.append(e)

        return len(nums)