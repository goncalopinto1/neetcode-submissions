class Solution {
public:
    bool isValid(string s) {
        stack<char> c;
        unordered_map<char, char> connections = {
            {')', '('},
            {'}', '{'},
           {']', '['}
        };

        for(char a : s){
            if(a == '(' || a == '{' || a == '['){
                c.push(a);
            } 
            else if ((a ==')' || a == '}' || a == ']')) {
                if(c.empty()) return false;
                
                char top = c.top();

                if(top != connections[a]) return false;

                c.pop();
            }
        }

        if(!c.empty()) return false;

        return true;
    }
};
