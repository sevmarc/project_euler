#include <iostream>
#include <vector>
#include <math.h>
using namespace std;


bool is_prime(unsigned int num) {
    if (num == 2) {
        return true;
    }
    for (unsigned int i = 2; i <= (sqrt(num) + 1); ++i) {
        if (num % i == 0) {
            return false;
        }
    }
    return true;
}

vector<unsigned int> primes(long long int orig) {
    vector<unsigned int> primes;

    while (orig != 1) {
        if (is_prime(orig)) {
            primes.push_back(orig);
            return primes;
        }
        for (unsigned int i=2; i <= orig; ++i) {
            if ((orig % i == 0) && is_prime(i)) {
                orig = (long int)(orig) / i;
                primes.push_back(i);
                break;
            }
        }
    }
    return primes;
}

unsigned int max_vector(vector <unsigned int> vec) {
    unsigned int vec_max = 0;
    for (int i = 0; i < vec.size(); i++)
        if (vec[i] > vec_max)
            vec_max = vec[i];
    return vec_max;
}

int main() {
    long long int input_val = 600851475143;
    vector<unsigned int> primes_result = primes(input_val);
    
    bool printer = true;

    if (printer) {
        cout << "Prime divisors: \n";
        for (auto i = primes_result.begin(); i != primes_result.end(); ++i)
            cout << *i << "\n";
    }
    cout << "Max: " << max_vector(primes_result) << "\n";
    return 0;
}
