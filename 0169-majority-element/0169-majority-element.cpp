class Solution {
public:
    int majorityElement(vector<int>& nums) {
        map<int, int> map;
        for(int i = 0; i < nums.size(); i++){
            map[nums[i]]++;

        }
        for(auto it: map){
            if(it.second > (nums.size()/ 2)){
                return it.first;
            }
        }
        return -1;
    }
};