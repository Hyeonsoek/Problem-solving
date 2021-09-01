#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int n,m,map[1001][1001];
int cache[1001][1001];

int candy(int x,int y) {
	if(x==n-1 && y==m-1) return map[x][y];
	if(x<0||y<0||x>=n||y>=m) return 0;
	int &ret = cache[x][y];
	if(ret!=-1) return ret;
	return ret = max({candy(x,y+1),candy(x+1,y),candy(x+1,y+1)})+map[x][y];
}

int main() {
	memset(cache,-1,sizeof(cache));
	scanf("%d%d",&n,&m);
	for(int i=0; i<n; i++) {
		for(int j=0; j<m; j++) {
			scanf("%d",&map[i][j]);
		}
	} printf("%d\n",candy(0,0));
}