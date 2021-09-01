#include <cstdio>
#include <cstring>
int n,m,k,len;
char input[101][101];
char find[81];
int cache[101][101][81];
int dir[4][2] = {{1,0},{0,1},{-1,0},{0,-1}};

int solve(int x,int y,int z) {
	if(z == len-1) return 1;
	int &ret = cache[x][y][z];
	if(ret != -1) return ret;
	ret = 0;
	for(int i=0; i<4; i++) {
		for(int j=1; j<=k; j++) {
			int xx = x + dir[i][0]*j;
			int yy = y + dir[i][1]*j;
			if(xx < 0 || xx >= n || yy < 0 || yy >= m)
				continue;
			if(input[xx][yy] != find[z+1])
				continue;
			ret += solve(xx,yy,z+1);
		}
	} return ret;
}

int main() {
	memset(cache,-1,sizeof(cache));
	scanf("%d%d%d",&n,&m,&k);
	for(int i=0; i<n; i++) {
		scanf("%s",input[i]);
	}scanf("%s",find);
	len = strlen(find);
	int ans = 0;
	for(int i=0; i<n; i++) {
		for(int j=0; j<m; j++) {
			if(find[0]==input[i][j]) ans+=solve(i,j,0);
		}
	}printf("%d\n",ans);
}