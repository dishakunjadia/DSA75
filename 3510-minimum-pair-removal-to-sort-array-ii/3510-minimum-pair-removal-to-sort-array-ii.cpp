#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    int minimumPairRemoval(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return 0;

        // Doubly linked list
        vector<int> left(n), right(n);
        vector<bool> alive(n, true);

        for (int i = 0; i < n; i++) {
            left[i] = i - 1;
            right[i] = (i + 1 < n ? i + 1 : -1);
        }

        // Count decreasing violations
        int bad = 0;
        for (int i = 0; i + 1 < n; i++) {
            if (nums[i] > nums[i + 1]) bad++;
        }

        // Min-heap: (sum, index)
        priority_queue<
            pair<long long, int>,
            vector<pair<long long, int>>,
            greater<pair<long long, int>>
        > pq;

        for (int i = 0; i + 1 < n; i++) {
            pq.push({(long long)nums[i] + nums[i + 1], i});
        }

        auto is_bad = [&](int i, int j) {
            return i != -1 && j != -1 && nums[i] > nums[j];
        };

        int ops = 0;

        while (bad > 0) {
            auto top = pq.top();
            pq.pop();

            int i = top.second;
            int j = right[i];

            // Skip stale entries
            if (j == -1 || !alive[i] || !alive[j]) continue;

            // Remove old violations
            if (is_bad(left[i], i)) bad--;
            if (is_bad(i, j)) bad--;
            if (is_bad(j, right[j])) bad--;

            // Merge i and j
            nums[i] += nums[j];
            alive[j] = false;

            right[i] = right[j];
            if (right[j] != -1) {
                left[right[j]] = i;
            }

            // Add new violations
            if (is_bad(left[i], i)) bad++;
            if (is_bad(i, right[i])) bad++;

            // Push updated adjacent sums
            if (left[i] != -1) {
                pq.push({(long long)nums[left[i]] + nums[i], left[i]});
            }
            if (right[i] != -1) {
                pq.push({(long long)nums[i] + nums[right[i]], i});
            }

            ops++;
        }

        return ops;
    }
};
