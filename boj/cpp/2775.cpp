#include <cstdio>
#include <cstring>

int map[16][16];

int solve(int k,int n) {
	int &ret=map[k][n];
	if(ret!=-1) return ret;
	ret = 0;
	for(int i=1; i<=n; i++)
		ret += solve(k-1,i);
	return ret;
}

int main() {
	memset(map,-1,sizeof(map));
	for(int i=1; i<16; i++)
		map[0][i]=i;
	for(int i=0; i<16; i++)
		map[i][1]=1;
	int N;
	for(scanf("%d",&N);N--;) {
		int k,n;
		scanf("%d%d",&k,&n);
		printf("%d\n",solve(k,n));
	}
}