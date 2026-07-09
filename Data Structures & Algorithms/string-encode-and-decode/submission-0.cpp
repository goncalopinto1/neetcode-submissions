class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded;
        for(string s : strs){
            encoded += to_string(s.length()) + "#" + s;
        }
        return encoded;
    }

    vector<string> decode(string s) {
        vector<string> result;
        int i = 0;
        int n = s.length();

        while(i < n){
            int delimeter = s.find('#', i);

            int size = stoi(s.substr(i, delimeter - i));

            i = delimeter + 1;
            result.push_back(s.substr(i, size));

            i += size;
        }

        return result;
    }
};
