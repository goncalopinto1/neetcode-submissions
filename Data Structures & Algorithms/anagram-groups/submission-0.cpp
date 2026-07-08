class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result;

        map<array<int, 26>, vector<string>> anagram;
        // O(m * n)
        for(string s : strs){
            array<int, 26> p = {0};

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
