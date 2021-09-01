#include <cstdio>
#include <cmath>
#include <cstring>
long long N,temp;
long long sam[20];
int cache[20];

int dp(int n,long long cur)
{
	if(n == 20)
	{
		if(cur == N) return true;
		else return false;
	}
	int ret = 0;
	if(n + 1 <= 20)
		ret |= dp(n+1,cur+sam[n]);
	ret |= dp(n+1,cur);

	return ret;
}
int main()
{
	scanf("%lld",&N);
	for(int i=0; i<20; ++i)
		sam[i] = pow(3,i);
	memset(cache,-1,sizeof(cache));
	if(N == 0)
	{
		printf("NO\n");
		return 0;
	}
	printf("%s\n",dp(0,0)?"YES":"NO");
}