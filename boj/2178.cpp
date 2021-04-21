#include <cstdio>
#include <queue>
using namespace std;
int N,M,check[101][101];
char s[101][101]={};
int bfs(){
	int dir[4][2] = {{0,1},{0,-1},{1,0},{-1,0}};
	queue< pair<int,int> > q;
	q.push(make_pair(0,0));
	check[0][0] = 1;
	while (!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop();
		for (int i=0;i<4;i++) {
			int xx = x+dir[i][0];
			int yy = y+dir[i][1];
			if (xx>=0 && xx<N && yy>=0 && yy<M && check[xx][yy]==0 && s[xx][yy]=='1') {
				check[xx][yy]=check[x][y]+1;
				q.push(make_pair(xx,yy));
			}
		}
	} printf("%d",check[N-1][M-1]);
}
int main() {
	scanf("%d%d",&N,&M);
	for (int i=0; i<N; i++) {
		scanf("%s",s[i]);
	} bfs();
}
