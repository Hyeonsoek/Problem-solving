#include <cstdio>
#include <cstring>
#define min(a,b) (a>b?b:a)
#define MAX 987654321

int n;
int Map[16][16];
int dist[16][1<<16];

int dp(int start,int check)
{
	if(check == (1<<n)-1)
	{	if(!Map[start][0]) return INF;
		else return Map[start][0];
	}

	int &ret = dist[start][check];
	if(ret != -1)
		return ret;

	ret = MAX;
	for(int i=0; i<n; ++i)
		if((check & (1<<i)) == 0 && Map[start][i])
			ret = min(ret,dp(i,check|(1<<i))+Map[start][i]);
	return ret;
}

int main()
{
	scanf("%d",&n);
	for(int i=0; i<n; ++i)
		for(int j=0; j<n; ++j)
			scanf("%d",&Map[i][j]);
	memset(dist,-1,sizeof(dist));
	int ans = dp(0,1);
	printf("%d\n",ans);
}