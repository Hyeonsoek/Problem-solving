#include <cstdio>
#include <cmath>

int main() {
	int m,n,count=0;
	scanf("%d%d",&m,&n);
	int ms = (int)ceil(sqrt(m)),ns = (int)floor(sqrt(n));
	for(int i=ms; i<=ns; i++) {
		count+=i*i;
	}
	if(ns >= ms) printf("%d\n%d",count,ms*ms);
	else printf("-1");
}