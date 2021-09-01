#include <cstdio>

int main() {
	int N,max=0,a[1002]={},answer[1002]={};
	scanf("%d",&N);
	for(int i=0; i<N; i++) scanf("%d",&a[i]);

	for(int i=0; i<N; i++) {
		int temp=0,sum=0;
		for(int j=0; j<=i; j++) {
			if(a[i] > a[j]) {
				if(temp < answer[j]) {
					temp = answer[j];
				}
			}
 		}
 		answer[i] = temp + a[i];
 		if(max < answer[i]) max = answer[i];
	} printf("%d\n",max);
}
