class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;

        unordered_map<int, int> values; 
        
        for(int i = 0; i < nums.size(); i++){
            int compensation = target - nums[i];

            if(values.count(compensation)){
                if(i < values[compensation]) {
                    result.push_back(i);
                    result.push_back(values[compensation]);
                    return result;
                }
                    result.push_back(values[compensation]);
                    result.push_back(i);
                    return result;
            }
            values[nums[i]] = i;
        }
        return result;
    }
};
