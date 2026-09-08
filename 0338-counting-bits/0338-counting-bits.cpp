class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> result(n+1);

        if (n == 0)
        return result;

        for (int i =0; i < n + 1; i++) {
            result[i] = result[i>>1] + (i & 1);
        }
        return result;
    }
    
};