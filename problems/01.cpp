#include <iostream>
using namespace std;

int div_by_3_or_5(int x) {
    int sum = 0;
    for (int i = 0; i < x; i++) {
        if (i % 3 == 0 || i % 5 == 0) {
            sum += i;
        }
    }
    return sum;
}

int main() {
    int n = 1000;
    int result = div_by_3_or_5(n);
    cout << result << '\n';
    return 0;
}
