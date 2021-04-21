#include <cstdio>
int main() {
	int N,M,K;
	scanf("%d%d%d",&N,&M,&K);
	for(int i=0; i<K; i++)
		N = N xor M;
	printf("%d",N);
}
