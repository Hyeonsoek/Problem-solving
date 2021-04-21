#include <iostream>
using namespace std;
int main() {
	int N,i=1,j=0,a,b;
	cin >> N;
	while(N!=0) {
		if((N-i)<0) {
			j = N;
			break;
		}
		if((N-i)==0) {
			break;
		}
		if((N-i)>0) {
			N-=i;
			i++;
		}
	}
	if(j!=0){
		a = i,b = 1;
		for(int k=j; k>1; k--) {
			a--,b++;
		} if(i%2==0) {
			cout << b << '/' << a;
		} else {
			cout << a << '/' << b;
		}
	} else {
		if(i%2==1) {
			cout << 1 << '/' << i;
		} else {
			cout << i << '/' << 1;
		}
	}
}
