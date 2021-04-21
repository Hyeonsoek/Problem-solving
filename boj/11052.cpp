#include <cstdio>
#include <cstring>
#define INF -987654321
#define max(a,b) a>b?a:b
int N,card[1001];
int cache[1001][1001];
int cost = INF;

int solve(int card,int num)
{
	if(card > N) return 0;
	if(card == N) return card[num];
	int &ret = cache[card][num];
	if(ret != -1)
		return ret;
	for(int i=0; i<N; i++)
		ret = max()
}

int main()
{
	memset(cache,-1,sizeof(cache));
	scanf("%d",&N);
	for(int i=0; i<N; ++i)
	{
		scanf("%d",&card[i]);
	}
	printf("%d",solve(0,0));
}