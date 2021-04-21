#include <cstdio>
int N,c1,c2,a,b;

int main() {
	for(scanf("%d",&N);N--;){
		scanf("%d%d",&a,&b);
		if (a>b) c1++;
		if (b>a) c2++;
	}
	printf("%d %d",c1,c2);
}
