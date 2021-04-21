#include <cstdio>
int main() {
	int N,K;
	scanf("%d%d",&N,&K);
	for(int i = 0; i < 5; i++) {
		int L;
		scanf("%d",&L);
		printf("%d ",L-N*K);
	}
}
