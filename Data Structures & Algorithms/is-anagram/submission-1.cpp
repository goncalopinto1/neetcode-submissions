class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> values;

        for(char c : s){
            values[c]++;
        }

        for(char c : t){
            values[c]--;
        }

        for(auto const [key, value] : values){
            if (value != 0) {
                return false;
            }
        }

        return true;
    }
};
