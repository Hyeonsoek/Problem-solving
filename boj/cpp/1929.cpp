#include <cstdio>
int prim[1000001];
int main() {
	int N,M,min=999999,count=0;
	scanf("%d%d",&N,&M);
	for (int i = 2; i <= M; i++) {
		if (prim[i]==0) {
			if (N<=i) count+=i;
			if (N<=i && min>i) min=i;
			for (int j = 2*i; j <= M; j+=i) {
				prim[j]=1;
			}
		}
	}
	if (count!=0) printf("%d\n%d",count,min);
	else printf("-1");
}
