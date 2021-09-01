#include <cstdio>

int main() {
	int a[6];
	for(int i=0; i<5; i++)
		scanf("%d",&a[i]);
	for(int i=1;;i++) {
		int count=0;
		for(int j=0; j<5; j++) {
			if(i%a[j]==0)
				count++;
		}
		if(count >= 3) {
			printf("%d",i);
			break;
		}
	}
}