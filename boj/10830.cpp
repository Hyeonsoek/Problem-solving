#include <cstdio>
#include <vector>
using namespace std;
typedef vector<vector<long long> > maxtrix;
long long A,B;

maxtrix operator *(const maxtrix &a,const maxtrix &b) {
	int size = a.size();
	maxtrix c(size,vector<long long>(size));
	for(int i=0; i<size; i++) {
		for(int j=0; j<size; j++) {
			for(int k=0; k<size; k++) {
				c[i][j] += (a[i][k]*b[k][j])%1000;
				c[i][j] %= 1000;
			} c[i][j] %= 1000;
		}
	} return c;
}

int main() {
	scanf("%lld%lld",&A,&B);
	maxtrix a(A,vector<long long>(A));
	maxtrix ans(A,vector<long long>(A));
	for(int i=0; i<A; i++) ans[i][i] = 1;
	for(int i=0; i<A; i++) {
		for(int j=0; j<A; j++) {
			long long input; scanf("%lld",&input);
			a[i][j] = input;
		}
	}
	while(B>0) {
		if(B%2 == 1) {
			ans = ans * a;
		} a = a*a;
		B/=2;
	}
	for(int i=0; i<A; i++) {
		for(int j=0; j<A; j++) {
			if(j < A-1)
				printf("%lld ",ans[i][j]);
			else printf("%lld",ans[i][j]);
		}printf("\n");
	}
}
