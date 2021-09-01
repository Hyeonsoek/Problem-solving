#include <cstdio>
long long dp[101];

long long solve(int n) {
	if(n <= 3) return 1;
	if(n == 4 || n == 5) return 2;

	long long &ret = dp[n];
	if(ret != 0) return ret;
	return ret = solve(n-1)+solve(n-5);
}

int main() {
	int n;
	for(scanf("%d",&n);n--;) {
		int t;
		scanf("%d",&t);
		printf("%lld\n",solve(t));
	}
}
