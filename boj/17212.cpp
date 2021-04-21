#include <cstdio>
#include <cstring>
#define min(a,b) ((a>b)?b:a)
#define MAX (1<<30)
int cache[100001],N;
int coin[4] = {1,2,5,7};

int dp(int N)
{
	if(N == 0)
		return 0;

	int &ret = cache[N];
	if(ret != -1)
		return ret;

	ret = MAX;
	for(int i=0; i<4; ++i)
		if(N >= coin[i])
			ret = min(ret,dp(N-coin[i])+1);
	return ret;
}

int main()
{
	scanf("%d",&N);
	memset(cache,-1,sizeof(cache));
	printf("%d\n",dp(N));
}