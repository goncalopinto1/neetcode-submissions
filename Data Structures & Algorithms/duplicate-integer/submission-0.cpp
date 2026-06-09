class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> frequency;

        for(int i : nums){
            if(frequency.count(i) == 1){
                return true;
            }

            frequency.insert(i);
        }

        return false;
    }
};