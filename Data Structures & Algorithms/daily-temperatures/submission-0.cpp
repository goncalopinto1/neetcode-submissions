class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> results(temperatures.size());
        stack<pair<int, int>> s;

        for(int i = 0; i < temperatures.size(); i++){
            if(s.empty()){
                s.push({temperatures[i], i});
            } else if(!(temperatures[i] > s.top().first)){
                s.push({temperatures[i], i});
            } else {
                while(!s.empty() && temperatures[i] > s.top().first){
                    auto [val, idx] = s.top();
                    s.pop();

                    results[idx] = i - idx;
                } 
                s.push({temperatures[i], i});
            }
        }

        while(!s.empty()){
            auto [val, idx] = s.top();
            s.pop();
            results[idx] = 0;
        }

        return results;
    }
};
