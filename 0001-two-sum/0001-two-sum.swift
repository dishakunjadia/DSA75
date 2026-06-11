class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var map: [Int: Int] = [:]

        for (index, num) in nums.enumerated() {
            let complement = target - num

            if let complementIndex = map[complement] {
                return [complementIndex, index]
            }

            map[num] = index
        }

        return []
    }
}