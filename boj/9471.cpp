#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
	int T,N,K;
	for(cin >> T;T--;) {
		cin >> K >> N;
		int f1,f2,period=0;
		f1 = f2 = 1;
		
		do {
			int temp = f1;
			f1 = f2;
			f2 = (temp+f2)%N;
			period++;
		} while(!(f1==1&&f2==1));
		cout << K << ' ' << period << '\n';
	}
}
