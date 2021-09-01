#include <cstdio>
#include <queue>
using namespace std;
typedef pair<int,int> p;
int n;
int dir[4][2] = {{0,1},{1,0},{-1,0},{0,-1}};
char map[101][101];
char check_R[101][101];
char check_B[101][101];

void bfs(p start) {
	queue<p> q;
	q.push(start);
	int sx = start.first;
	int sy = start.second;
	char first = map[sx][sy];
	check_R[sx][sy]=1;
	while(!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop();
		for(int i=0; i<4; i++) {
			int xx = x + dir[i][0];
			int yy = y + dir[i][1];
			if(xx < 0 || xx >= n || yy < 0 || yy >= n)
				continue;
			if(check_R[xx][yy] || map[xx][yy] != first)
				continue;
			q.push(p(xx,yy));
			check_R[xx][yy]=1;
		}
	}
}

void bfs_B(p start) {
	queue<p> q;
	q.push(start);
	int sx = start.first;
	int sy = start.second;
	char first = map[sx][sy];
	check_B[sx][sy]=1;
	while(!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop();
		for(int i=0; i<4; i++) {
			int xx = x + dir[i][0];
			int yy = y + dir[i][1];
			if(xx < 0 || xx >= n || yy < 0 || yy >= n)
				continue;
			if(first == 'R' || first == 'G') {
				if(check_B[xx][yy] || map[xx][yy] == 'B')
					continue;
			}
			else {
				if(check_B[xx][yy] || map[xx][yy] != first)
					continue;	
			}
			q.push(p(xx,yy));
			check_B[xx][yy]=1;
		}
	}
}

int main() {
	int cnt=0,cnt_B=0;
	scanf("%d",&n);
	for(int i=0; i<n; i++)
		scanf("%s",map[i]);
	for(int i=0; i<n; i++) {
		for(int j=0; j<n; j++) {
			if(!check_R[i][j]) {
				bfs(p(i,j));
				cnt++;
			}
			if(!check_B[i][j]) {
				bfs_B(p(i,j));
				cnt_B++;
			}
		}
	}
	printf("%d %d",cnt,cnt_B);
}
