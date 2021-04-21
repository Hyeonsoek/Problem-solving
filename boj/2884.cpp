#include<cstdio>
int main() {
	int N,M;
	scanf("%d%d",&N,&M);
	N = M-45<0?(N-1)<0?23:N-1:N;
	M = M-45<0?M+15:M-45;
	printf("%d %d",N,M);
}
