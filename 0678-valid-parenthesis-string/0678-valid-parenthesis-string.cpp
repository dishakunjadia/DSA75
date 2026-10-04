class Solution {
public:
    bool checkValidString(string s) {
        int cmin = 0; // Minimum possible open parentheses count
        int cmax = 0; // Maximum possible open parentheses count
        
        for (char c : s) {
            if (c == '(') {
                cmin++;
                cmax++;
            } else if (c == ')') {
                cmin = std::max(0, cmin - 1);
                cmax--;
            } else { // c == '*'
                cmin = std::max(0, cmin - 1); // Treat '*' as ')'
                cmax++;                        // Treat '*' as '('
            }
            
            if (cmax < 0) {
                return false; // Too many closing parentheses
            }
        }
        
        return cmin == 0;
    }
};