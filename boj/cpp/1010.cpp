#include <cstdio>
int main() {
	int N;
	for(scanf("%d",&N);N--;){
		int K,M,count=0;
		scanf("%d%d",&K,&M);
		long comb[101][101]={};
		for (int i=0; i<=M; i++) {
			comb[0][i]=1;
		} for (int i=0; i<=K; i++) {
			comb[i][0]=1;
		} for (int i=1; i<=K; i++) {
			for (int j=1; j<M; j++) {
				comb[i][j]=comb[i-1][j]+comb[i][j-1];
			}
		} printf("%ld\n",comb[K][M-K]);
	}
}
