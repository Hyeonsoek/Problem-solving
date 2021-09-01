#include <cstdio>
int main() {
	int n;
	scanf("%d",&n);
	printf("%d",n/5+(n>=25?n/25:0)+(n>=125?n/125:0));
}