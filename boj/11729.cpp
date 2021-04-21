#include <cstdio>
#include <cmath>
int N;
void hinoi(int N,int a,int b,int c) {
	if (N == 0) {
		printf("%d %d\n",a,b);
		return;
	} else {
		hinoi(N-1,a,c,b);
		printf("%d %d\n",a,b);
		hinoi(N-1,c,b,a);
	}
	
}
int main() {
	scanf("%d",&N);
	printf("%d\n",(int)(pow(2,N)-1));
	hinoi(N-1,1,3,2);
}
