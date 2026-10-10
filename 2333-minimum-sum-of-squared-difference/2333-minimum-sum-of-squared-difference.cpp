
class Solution {
public:
    long long minSumSquareDiff(vector<int>& nums1, vector<int>& nums2, int k1, int k2) {
        int n = nums1.size();
        long long k = (long long)k1 + k2;
        
        // The maximum possible element is 10^5, so maximum difference is 10^5
        vector<long long> bucket(100001, 0);
        long long total_diff = 0;
        int max_diff = 0;
        
        // Step 1: Calculate absolute differences and populate the frequency bucket
        for (int i = 0; i < n; ++i) {
            int diff = abs(nums1[i] - nums2[i]);
            if (diff > 0) {
                bucket[diff]++;
                total_diff += diff;
                max_diff = max(max_diff, diff);
            }
        }
        
        // If our total budget can reduce all differences to 0, return 0
        if (total_diff <= k) {
            return 0;
        }
        
        // Step 2: Greedy reduction from the maximum difference downwards
        for (int d = max_diff; d > 0 && k > 0; --d) {
            if (bucket[d] > 0) {
                // How many elements we can completely shift from difference 'd' to 'd-1'
                long long take = min(k, bucket[d]);
                bucket[d] -= take;
                bucket[d - 1] += take;
                k -= take;
            }
        }
        
        // Step 3: Compute the final minimum sum of squared differences
        long long ans = 0;
        for (long long d = 1; d <= max_diff; ++d) {
            if (bucket[d] > 0) {
                ans += bucket[d] * d * d;
            }
        }
        
        return ans;
    }
};
