#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
	int N,P[1001],num=0;
	scanf("%d",&N);
	for(int i=0; i<N; i++) {scanf("%d",&P[i]);}
	sort(P,P+N);
	for(int i=0; i<N; i++) {
		for(int j=0; j<=i; j++) {num += P[j];}
	} printf("%d",num);
}
