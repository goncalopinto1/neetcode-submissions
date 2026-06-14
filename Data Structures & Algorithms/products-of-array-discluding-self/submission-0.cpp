class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int size = nums.size();
        vector<int> r(size);
        vector<int> p(size + 1);
        p[0] = 1;
        for(int i = 0; i < size; i++){
            p[i + 1] = p[i] * nums[i];
        }

        vector<int> s(size + 1);
        s[size] = 1;
        for(int j = size; j > 0; j--){
            s[j - 1] = s[j] * nums[j - 1];
        }

        for(int k = 0; k < size; k++){
            r[k] = p[k] * s[k + 1];
        }

        return r;
    }
};
