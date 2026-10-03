class Solution {
public:
    int longestValidParentheses(string s) {
        
        int left = 0, right = 0, maxLength = 0;
        int n = s.length();

        // First pass: Left to Right
        for (int i = 0; i < n; i++) {
            if (s[i] == '(') {
                left++;
            } else {
                right++;
            }

            if (left == right) {
                maxLength = std::max(maxLength, left + right);
            } else if (right > left) {
                left = 0;
                right = 0;
            }
        }

        // Reset counters for the reverse pass
        left = 0;
        right = 0;

        // Second pass: Right to Left
        for (int i = n - 1; i >= 0; i--) {
            if (s[i] == '(') {
                left++;
            } else {
                right++;
            }

            if (left == right) {
                maxLength = std::max(maxLength, left + right);
            } else if (left > right) {
                left = 0;
                right = 0;
            }
        }
        return maxLength;

    }
};