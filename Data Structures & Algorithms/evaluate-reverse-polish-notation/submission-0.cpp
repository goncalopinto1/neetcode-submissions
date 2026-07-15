class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> operands;

        unordered_map<string, function<int(int, int)>> operatorMap = {
            {"+", [](int a, int b) {return a + b;}},
            {"-", [](int a, int b) {return a - b;}},
            {"*", [](int a, int b) {return a * b;}},
            {"/", [](int a, int b) {return b != 0 ? a / b : 0 ;}},
        };

        for(auto elem : tokens){
            if(elem != "+" && elem != "-"  && elem != "*" && elem != "/"){
                operands.push(stoi(elem));
            } else {
                int secondOperand = operands.top();
                operands.pop();

                int firstOperand = operands.top();
                operands.pop();

                int result = operatorMap[elem](firstOperand, secondOperand);
                operands.push(result);
            }
        }

        return operands.top();
    }
};
