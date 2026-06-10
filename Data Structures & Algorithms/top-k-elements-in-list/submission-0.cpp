class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> result;

        vector<vector<int>> freq(nums.size() + 1);
        unordered_map<int, int> tmp;

        for(int num : nums){
            tmp[num]++;
        }

        for(auto const [key, value] : tmp){
            freq[value].push_back(key);
        }

        for(int i = freq.size() - 1; i >= 0; i--){
            for(int n : freq[i]){
                if(k > 0){
                    result.push_back(n);
                    k--;
                }
            }
        }

        return result;
    }
};
