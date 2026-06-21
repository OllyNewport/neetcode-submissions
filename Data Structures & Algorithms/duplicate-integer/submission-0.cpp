class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        for (int num : nums) {
            int count = 0;

            for (int n : nums) {
                if (num == n) {
                    count += 1;
                }
            }
            if (count > 1) {
                return true;
            }
        }
        
        return false;
    }
};