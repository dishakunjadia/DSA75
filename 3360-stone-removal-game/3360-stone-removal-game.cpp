class Solution {
public:
    bool canAliceWin(int n) {
        int count = 0;
        int stones = 10; 
        while(1){
            if (stones <= n){
                n -= stones; 
                stones--;
                count++;

            } 
            else {
                break;
            }
        }
        if (count % 2 == 0){
            return false;
        }
        else {
            return true;
        }
    }
};