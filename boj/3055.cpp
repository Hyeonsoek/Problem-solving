#include <cstdio>
#include <queue>
using namespace std;
int N,M,dir[4][2]={{0,1},{0,-1},{1,0},{-1,0}},check[51][51];
char map[51][51];
pair<int,int> start,end;
queue< pair<int,int> > q,star;
void bfs() {
	q.push(start);
	check[start.first][start.second] = 1;
	while (!q.empty()) {
		int qsize = q.size(),ssize = star.size(),bre=0;
		for (int i = 0; i < ssize; i++) {
			int x = star.front().first;
			int y = star.front().second;
			star.pop();
			for (int j = 0; j < 4; j++) {
				int xx = x + dir[j][0];
				int yy = y + dir[j][1];
				if (xx>=0 && xx<N && yy>=0 && yy<M
						&&(map[xx][yy]=='S'||map[xx][yy]=='.')) {
					map[xx][yy] = '*';
					star.push(make_pair(xx,yy));
				}
			}
		}
		for (int i = 0; i < qsize; i++) {
			int x = q.front().first;
			int y = q.front().second;
			q.pop();
			if (x == end.first && y == end.second) {
				bre = 1; break;
			} for (int j = 0; j < 4; j++) {
				int xx = x + dir[j][0];
				int yy = y + dir[j][1];
				if (xx>=0 && xx<N && yy>=0 && yy<M
						&&!check[xx][yy] && map[xx][yy]!='*' && map[xx][yy]!='X') {
					map[xx][yy] = 'S';
					check[xx][yy] = check[x][y]+1;
					q.push(make_pair(xx,yy));
				}
			}
		}
		if (bre) break;
	} int temp = check[end.first][end.second]-1;
	if (temp > 0) printf("%d",temp);
	else printf("KAKTUS");
}
int main() {
	scanf("%d%d",&N,&M);
	for (int i = 0; i < N; i++) {
		scanf("%s",map[i]);
		for (int j = 0; j < M; j++) {
			if (map[i][j]=='S')
				start = make_pair(i,j);
			if (map[i][j]=='D')
				end = make_pair(i,j);
			if (map[i][j]=='*') {
				star.push(make_pair(i,j));
			}
		}
	} bfs();
}
