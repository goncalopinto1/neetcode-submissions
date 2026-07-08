class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result;

        unordered_map<string, vector<string>> anagram;
        //0(m * n)
        for(string s : strs){
            string p(26, 0);

            for(char a : s){
                a = tolower(a);

                p[a - 'a']++;
            }

            anagram[p].push_back(s);
        }

        for(auto val : anagram){
            result.push_back(val.second);
        }

        return result;
    }
};
