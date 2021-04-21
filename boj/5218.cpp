#include <cstdio>
#include <cstring>

int main() {
	int T;
	for(scanf("%d",&T);T--;){
		char a[21],b[21];
		scanf("%s%s",a,b);
		printf("Distances:");
		for(int i=0; i<strlen(a); i++) {
			printf(" %d",b[i]-a[i] < 0 ? 26+b[i]-a[i] : b[i]-a[i]);
		}printf("\n");
	}
}