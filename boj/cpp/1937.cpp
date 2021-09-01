#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int N,dir[4][2]={{0,1},{1,0},{-1,0},{0,-1}};
int tree[501][501];
int cache[501][501];

int solve(int x,int y) {
	int &ret = cache[x][y];
	if(ret != -1) return ret;
	ret = 1;
	for(int i=0; i<4; i++) {
		int xx = x + dir[i][0];
		int yy = y + dir[i][1];
		if(xx >= 0 && xx < N && yy >= 0 && yy < N && tree[xx][yy] > tree[x][y]) {
			ret = max(ret,1+solve(xx,yy));
		}
	} return ret;
}

int main() {
	scanf("%d",&N);
	for(int i=0; i<N; i++) {
		for(int j=0; j<N; j++) {
			scanf("%d",&tree[i][j]);
		}
	}
	memset(cache,-1,sizeof(cache));
	int ans = 0;
	for(int i=0; i<N; i++) {
		for(int j=0; j<N; j++) {
			ans = max(ans,solve(i,j));
		}
	} printf("%d\n",ans);
}
