#include <cstdio>
typedef long long int lld;
lld N,fib[1001]={0,1};

void fibo(int i) {
	if(i<=N) {
		fib[i] = fib[i-1] + fib[i-2];
		fibo(i+1);
	}
}

int main() {
	scanf("%d",&N);
	fibo(2);
	printf("%lld",fib[N]);
}
