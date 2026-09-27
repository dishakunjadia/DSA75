class Solution {
public:
    string reverseParentheses(string s) {

        int n = s.length();
        std::vector<int> pair(n);
        std::stack<int> st;

        for (int i = 0; i < n; ++i) {
            if (s[i] == '(') {
                st.push(i);
            } else if (s[i] == ')') {
                int j = st.top();
                st.pop();
                pair[j] = i;
                pair[i] = j;
            }
        }


        std::string result = "";
        int i = 0, direction = 1;
        while (i < n) {
            if (s[i] == '(' || s[i] == ')') {
                i = pair[i];
                direction = -direction;
            } else {
                result += s[i];
            }
            i += direction;
        }

        return result;
    }
};

