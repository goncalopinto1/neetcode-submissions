class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        for(int val = 0; val < nums.size(); val++){
            for(int val2 = val + 1; val2 < nums.size(); val2++){
                if((val != val2) && (nums[val] + nums[val2] == target)){
                    result.push_back(val);
                    result.push_back(val2);
                    return result;
                }
            }
        }
        return result;
    }
};
