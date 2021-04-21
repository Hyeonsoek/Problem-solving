#include <cstdio>
#include <queue>
#include <cstring>
using namespace std;

typedef pair<int,int> p;

char map[51][51];
int dir[4][2] = {{0,1},{1,0},{-1,0},{0,-1}};
int n,m;
int maxi=-1;
int bmax=-1;

int bfs(p start) {
	queue<p> q;
	int check[51][51]={};
	q.push(start);
	int sx = start.first;
	int sy = start.second;
	check[sx][sy] = 1;
	while(!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop();
		for(int i=0; i<4; i++) {
			int xx = x + dir[i][0];
			int yy = y + dir[i][1];
			if(xx < 0 || xx >= n || y < 0 || y >= m)
				continue;
			if(check[xx][yy] || map[xx][yy]!='L')
				continue;
			q.push(p(xx,yy));
			check[xx][yy] = check[x][y] + 1;
			if(check[xx][yy] > bmax)
				bmax = check[xx][yy];
		}
	}
	return bmax-1;
}

int main() {
	scanf("%d%d",&n,&m);
	for(int i=0; i<n; i++)
		scanf("%s",map[i]);
	for(int i=0; i<n; i++) {
		for(int j=0; j<m; j++) {
			if(map[i][j]=='L') {
				int b = bfs(p(i,j));
				if(b > maxi)
					maxi = b;
			}
		}
	}
	printf("%d",maxi);
}
