#include <cstdio>
int main() {
	int N,count=2;
	scanf("%d",&N);
	while (N!=1) {
		if (N%count==0) {
			N/=count;
			printf("%d\n",count);
		} else {
			count++;
		}
	}
}
