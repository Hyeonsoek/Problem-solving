#include <cstdio>
int main() {
	int N,count=1;
	scanf("%d",&N);
	for (int i = 1; i <= N; i++) {
		count*=i;
	} printf("%d",count);
}
