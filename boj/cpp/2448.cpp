#include <cstdio>

int main() {
	int n;
	scanf("%d",&n);
	for(int i=0; i<3; i++) {
		for(int j=2; j>i; j--) {
			printf(" ");
		}
		for(int j=0; j<=i; j++) {
			if(j==i && i==1)
				printf(" ");
			else printf("*");
		}
		for(int j=0; j<i; j++) {
			printf("*");
		}
		for(int j=2; j>i; j--) {
			printf(" ");
		}
		printf("\n");
	}
}
