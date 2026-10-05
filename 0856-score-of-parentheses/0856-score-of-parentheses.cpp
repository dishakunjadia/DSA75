class Solution {
public:
    int scoreOfParentheses(string s) {
        std::stack<int> st;
        st.push(0); // Base score for the current level

        for (char c : s) {
            if (c == '(') {
                st.push(0); // Enter a new nested level
            } else {
                int inner = st.top();
                st.pop();
                int outer = st.top();
                st.pop();
                
                // If inner is 0, it's a "()", score is 1. Otherwise, double the inner score.
                st.push(outer + std::max(2 * inner, 1));
            }
        }

        return st.top();
    }
};