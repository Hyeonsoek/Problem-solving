#include <cstdio>
#include <cstring>
#define max(a,b) (a>b?a:b)

int N,M,K;
int order[301][2];
int cache[100][301][301];

int dp(int start,int burgur,int potato)
{
	if(start == N)
		return 0;

	int &ret = cache[start][burgur][potato];
	if(ret != -1)
		return ret;

	int temp = -1;
	if(burgur >= order[start][0] && potato >= order[start][1])
	{
		temp = dp(start+1,burgur-order[start][0],potato-order[start][1]);
		ret = max(ret,temp+1);
	}
	temp = dp(start+1,burgur,potato);
	ret = max(ret,temp);
	return ret;
}

int main()
{
	scanf("%d%d%d",&N,&M,&K);
	memset(cache,-1,sizeof(cache));
	for(int i=0; i<N; ++i)
		scanf("%d%d",&order[i][0],&order[i][1]);
	int DPANS = dp(0,M,K);
	printf("%d\n",DPANS);
}