#include <iostream>
using namespace std;
const int A = 1000000;
const int p = A/10*15;
int fibo[p] = {0,1};
int main() {
	long long n;
	cin >> n;
	for(int i=2; i<p; i++) {
		fibo[i] = fibo[i-1]+fibo[i-2];
		fibo[i] %= A;
	} cout << fibo[n%p] << '\n';
}
