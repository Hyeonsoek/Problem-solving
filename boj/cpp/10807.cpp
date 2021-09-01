#include <cstdio>
#include <string>
int main() {
	int N,K,array[101],count=0;
	scanf("%d",&N);
	for(int i = 0; i < N; i++) {
		scanf("%d",&array[i]);
	} scanf("%d",&K);
	for (int i = 0; i < N; i++) {
		if (array[i]==K) count++;
	} printf("%d",count);
}
