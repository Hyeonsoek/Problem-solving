#include <cstdio>
#include <cstring>
int map[501][501];
int cache[501][501];
int n,m;
int dir[4][2] = {{0,1},{1,0},{-1,0},{0,-1}};

int solve(int x,int y) {
	if(x == n-1 && y == m-1) return 1;
	int &ret = cache[x][y];
	if(ret != -1) return ret;
	ret = 0;
	for(int i=0; i<4; i++) {
		int xx = x + dir[i][0];
		int yy = y + dir[i][1];
		if(xx >= 0 && xx < n && yy >= 0 && yy < m && map[xx][yy] < map[x][y]) {
			ret += solve(xx,yy);
		}
	} return ret;
}

int main() {
	scanf("%d%d",&n,&m);
	for(int i=0;i<n;i++) {
		for(int j=0;j<m;j++) {
			scanf("%d",&map[i][j]);
		}
	}
	memset(cache,-1,sizeof(cache));
	printf("%d",solve(0,0));
}