#include <cstdio>
int main() {
	int N,K,D[301],T=0;
	scanf("%d%d",&N,&K);
	for (int i = 1; i <= N; i++) {
		if (N % i == 0) D[T++] = i;
	}
	if (K > T) printf("0");
	else printf("%d",D[K-1]);
}
