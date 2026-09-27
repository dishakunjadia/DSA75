class Solution {
public:
    int minBitFlips(int start, int goal) {
        int xor_result = start ^ goal;
    int count = 0;
    while (xor_result > 0) {
        
        xor_result &= (xor_result - 1);
        count++;
    }   
        return count;
        }
};