#include <cstdio>
int main() {
	int N,K=0,count=1;
	scanf("%d",&N);
	K = (N%10)*10 + ((N%10+N/10) < 10 ? (N%10+N/10) : (N%10+N/10)%10);
	while (N!=K) {
		count++;
		K = (K%10)*10 + ((K%10+K/10) < 10 ? (K%10+K/10) : (K%10+K/10)%10);
	} printf("%d",count);
}
