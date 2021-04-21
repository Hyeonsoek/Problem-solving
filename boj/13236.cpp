#include <cstdio>
void func(int N) {
	printf("%d ",N);
	if (N==1) return;
	if (N%2==0) func(N/2);
	if (N%2==1) func(N*3+1);
}
int main() {
	int N;
	scanf("%d",&N);
	func(N);
}
