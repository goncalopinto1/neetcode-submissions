class MinStack {
    private:

    struct Element{
        int value;
        int min_here;
    };

    vector<Element> stack;

public:
    MinStack() {
    }
    
    void push(int val) {
        if(stack.empty()){
            stack.push_back({val, val});
        } else {
            int current_min = min(val, stack.back().min_here);
            stack.push_back({val, current_min});
        }
    }
    
    void pop() {
        if(!stack.empty()){
            stack.pop_back();
        }
    }
    
    int top() {
        return stack.back().value;
    }
    
    int getMin() {
        return stack.back().min_here;
    }
};
