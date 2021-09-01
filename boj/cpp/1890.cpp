#include <cstdio>
#include <cstring>
int n,Map[101][101];
int arrow[2][2] = {{0,1},{1,0}};
long long cache[101][101];

long long dp(int y,int x)
{
	if(x == n-1 && y == n-1 && !Map[y][x])
		return 1;

	long long &ret = cache[y][x];
	if(ret != -1)
		return ret;
	ret = 0;
	
	int xx1 = x + arrow[0][1]*Map[y][x];
	int yy1 = y + arrow[0][0]*Map[y][x];
	if(xx1 < n && yy1 < n)
		ret += dp(yy1,xx1);
	
	int xx2 = x+arrow[1][1]*Map[y][x];
	int yy2 = y+arrow[1][0]*Map[y][x];
	if(xx2 < n && yy2 < n)
		ret += dp(yy2,xx2);
	return ret;
}

int main()
{
	scanf("%d",&n);
	for(int i=0; i<n; ++i)
		for(int j=0; j<n; ++j)
			scanf("%d",&Map[i][j]);
	memset(cache,-1,sizeof(cache));
	long long cnt = dp(0,0);
	printf("%lld\n",cnt);
}