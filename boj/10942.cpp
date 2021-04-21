#include <cstdio>
#include <cstring>
int cache[2001][2001];
int ss[2001];
int n,m;

int solve(int s,int e) {
	if(s > e) return 1;
	int &ret = cache[s][e];
	if(ret != -1) return ret;
	if(ss[s] != ss[e]) return 0;
	return ret = solve(s+1,e-1);
}

int main() {
	memset(cache,-1,sizeof(cache));
	scanf("%d",&n);
	for(int i=0; i<n; i++) {
		scanf("%d",&ss[i]);
	} scanf("%d",&m);
	for(int i=0; i<m; i++) {
		int x,y;
		scanf("%d%d",&x,&y);
		printf("%d\n",solve(x-1,y-1));
	} 
}
