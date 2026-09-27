class Solution {
public:
    int minChanges(int n, int k) {
        if ((n & k) != k) {
            return -1;
        }
        int diff = n ^ k;
        int count = 0;

        while (diff > 0) {
            diff &= (diff - 1);
            count++;
        }
        return count;
    }
};