
class Solution {
public:
    vector<int> maxDepthAfterSplit(string seq) {
        vector<int> res;
        int depth = 0;
        for (char c : seq) {
            if (c == '(') {
                res.push_back(depth & 1);
                depth++;
            } else {
                depth--;
                res.push_back(depth & 1);
            }
        }
        return res;
    }
};
