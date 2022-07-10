#include <iostream>
#include <vector>
using namespace std;


// generic fibonacci function
vector<int> fibonacci(int limit) {
    vector<int> fibo;
    fibo.push_back(1);
    fibo.push_back(2);
    bool looking = true;

    int val = 0;
    int index = 2;
    while (val < limit) {
        val = fibo[index - 1] + fibo[index - 2];
        if (val > limit) {
            return fibo;
        }
        fibo.push_back(val);
        ++index;
    }
    return fibo;
}

int fibonacci_sum_even(int limit) {
    vector<int> fibo;
    fibo.push_back(1);
    fibo.push_back(2);

    int val = 0;
    int index = 2;
    int sum = 2;  // has to start from 2
    while (val < limit) {
        val = fibo[index - 1] + fibo[index - 2];            
        if (val > limit) {
            return sum;
        }
        fibo.push_back(val);
        if (val % 2 == 0) {
            // cout << val << ' ';
            sum += val;
        }
        ++index;
    }
    return sum;
}

int main() {
    vector<int> result = fibonacci(4000000);
    
    bool printer = false;

    if (printer) {
        cout << "Output of begin and end: ";
        for (auto i = result.begin(); i != result.end(); ++i)
            cout << *i << "\n";
    }
    
    int result_spec = fibonacci_sum_even(4000000);
    cout << "Result: " << result_spec << '\n';
    
    return 0;
}
