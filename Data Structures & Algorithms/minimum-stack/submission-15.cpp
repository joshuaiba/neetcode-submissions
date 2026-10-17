class MinStack {
vector<int> stackr;
vector<int> stack_min;
public:
    MinStack() {}
    
    void push(int val) {
        stackr.push_back(val);
        if (stack_min.empty()) {
            stack_min.push_back(val);
        } else if (val > stack_min.back()){
            stack_min.push_back(stack_min.back());
        } else {
            stack_min.push_back(val);
        }
    }
    
    void pop() {
        stackr.pop_back();
        stack_min.pop_back();
    }
    
    int top() {
        int val = stackr.back();
        return val;
    }
    
    int getMin() {
        int min_val = stack_min.back();
        return min_val;
    }
};
