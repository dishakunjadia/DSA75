class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int m = matrix[0].size();

        int left = 0; 
        int right = m -1;
        int top = 0;
        int bttom = n -1;

        vector<int> ans;
        while (top <= bttom && left <= right) {

        for(int i = left; i <= right; i++){
            ans.push_back(matrix[top][i]);
        }
        top++;
        for(int i = top; i <= bttom; i++){
            ans.push_back(matrix[i][right]);
        }
        right--;
        if (top <= bttom){
        for(int i = right; i >= left; i--){
            ans.push_back(matrix[bttom][i]);
            }
            bttom--;
        }
        if (left <= right){
        for(int i = bttom; i >= top; i--){
            ans.push_back(matrix[i][left]);
        }
        left++;
        }
    }
        return ans;
    }
};