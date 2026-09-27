class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        // Handle edge case: if the array is empty, return an empty string

        if (strs.empty()){
            return "";
        }
        std::string reference = strs[0];        

        for (size_t i = 0; i < reference.length(); i++) {
            char currentChar = reference[i];
            for (size_t j = 1; j < strs.size(); ++j) {
                if (i >= strs[j].length() || strs[j][i] != currentChar) {
                    return reference.substr(0, i);
                }
            }

        }
    
        return reference;
        }
};