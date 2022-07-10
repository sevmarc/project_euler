#include <iostream>
#include <vector>
using namespace std;

/* Largest palindrome product
A palindromic number reads the same both ways. The largest palindrome 
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
*/


int reversDigits(int num)
{
    int rev_num = 0;
    while (num > 0) {
        rev_num = rev_num * 10 + num % 10;
        num = num / 10;
    }
    return rev_num;
}

bool is_palindrome(int num) {
    return num == reversDigits(num);
}

vector<int> generate_products() {
    vector<int> products;
    for (int i = 100; i <= 999; ++i) {
        for (int j = 100; j <=999; ++j) {
            int prod = i * j;
            if ( is_palindrome(prod) ) {
                products.push_back(prod);
            }
        }
    }
    return products;
}

int max_vector(vector <int> vec) {
    int vec_max = 0;
    for (int i = 0; i < vec.size(); i++)
        if (vec[i] > vec_max)
            vec_max = vec[i];
    return vec_max;
}

int main() {
    vector<int> products = generate_products();
    cout << "Max: " << max_vector(products) << "\n";
    return 0;
}
