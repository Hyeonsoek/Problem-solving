#include <cstdio>

int main() {
	int max,N,num[100002]={},out[100002]={}; scanf("%d",&N);
	for(int i=1; i<=N; i++) scanf("%d",&num[i]);

	for(int i=1; i<=N; i++) {
		if(out[i-1] + num[i] > num[i]) {
			out[i] = out[i-1] + num[i];
		} else {
			out[i] = num[i];
		}
	} max = out[1];
	for(int i=2; i<=N; i++) {
		if(out[i] > max) max = out[i];
	} printf("%d",max);
}
