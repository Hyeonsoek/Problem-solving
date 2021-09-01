#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int N;
int map[301];
int dp[301];

int solve(int n,int c) {
	if(n == N) return map[n];
	int& ret = dp[n];
	if(ret != -1) {
		if((c == 2) && (n <= N-2))
			ret = max({ret,map[n] + solve(n+2,1)});
		if((c == 2) && (n > N-2));
		if((c == 1) && (n <= N-2))
			ret = max({ret,map[n] + solve(n+1,2),
							map[n] + solve(n+2,1)});
		if((c == 1) && (n > N-2))
			ret = max({ret,map[n] + solve(n+1,2)});
	}
	return ret;
}

int main() {
	scanf("%d",&N);
	for(int i=0; i<N; i++)
		scanf("%d",&map[i]);
	printf("%d",solve(0,1));
}
