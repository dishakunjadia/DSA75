class Solution {
    func maximumSum(_ nums: [Int]) -> Int {
        var rem0: [Int] = []
        var rem1: [Int] = []
        var rem2: [Int] = []

        for num in nums {
            switch num % 3 {
                case 0: rem0.append(num)
                case 1: rem1.append(num)
                default: rem2.append(num)
            }
        }
        rem0.sort(by: >)
        rem1.sort(by: >)
        rem2.sort(by: >)

        var ans = 0
        if rem0.count >= 3 {
            ans = max(ans, rem0[0] + rem0[1] + rem0[2])
        }

        if rem1.count >= 3 {
            ans = max(ans, rem1[0] + rem1[1] + rem1[2])
        }

        if rem2.count >= 3 {
            ans = max(ans, rem2[0] + rem2[1] + rem2[2])
        }

        if rem0.count >= 1 && rem1.count >= 1 && rem2.count >= 1 {
            ans = max(ans, rem0[0] + rem1[0] + rem2[0])
        }
        return ans
    }
}