#include <cstdio>
int main() {
	int var[1001]={},mid,max=-1,maxx=-1;
	for (int i = 0; i < 10; i++) {
		int N;
		scanf("%d",&N);
		mid += N;
		var[N]++;
	} for (int i = 10; i <= 1000; i+=10) {
		if (var[i] > max) {
			max = var[i];
			maxx = i;
		}
	} printf("%d\n%d",mid/10,maxx);
}
