#include <cstdio>
int main() {
	int max=-1,n,a[1002]={},answer[1002]={};
	scanf("%d",&n);
	for(int i=0; i<n; i++) {
		scanf("%d",&a[i]);
	}

	for(int i=0; i<n; i++) {
		int min = 0;
		for(int j=0; j<=i; j++) {
			if(a[j] < a[i]) {
				if (min < answer[j])
					min = answer[j];
			}
		} answer[i] = min + 1;
		if(max < answer[i]) {
			max = answer[i];
		}
	}

	printf("%d\n",max);
}
