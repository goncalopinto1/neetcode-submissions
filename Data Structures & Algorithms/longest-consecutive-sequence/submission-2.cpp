class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> s;
        int max_size = 0;

        for (int n : nums){
            s.insert(n);
        }

        for(int num : nums){ // O(n)
            int current_size = 1;

            auto it = s.find(num - 1);

            if(it != s.end()) continue;
            
            int next = num + 1;

            while(s.find(next) != s.end()) {
                next++;

                current_size++;

                s.erase(num);
            }

            if(current_size > max_size) max_size = current_size;
        }

        return max_size;
    }
};
