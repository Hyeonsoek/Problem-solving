#include <cstdio>
#include <queue>
#include <utility>
using namespace std;

typedef pair<int,int> p;
int map[1001][1001],check[1001][1001],M,N,days;
int dir[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
queue<p> q;

void BFS() {
	while(!q.empty()) {
		days++;
		int size = q.size();
		for(int i=0; i<size; i++) {
			int x = q.front().second;
			int y = q.front().first;
			q.pop();
			for(int j=0; j<4; j++) {
				int xx = x + dir[j][0];
				int yy = y + dir[j][1];
				if(xx >= 0 && xx < M && yy >= 0 && yy < N && !check[yy][xx] && map[yy][xx] == 0) {
					q.push(p(yy,xx));
					check[yy][xx] = 1;
					map[yy][xx] = 1;
				}
			}
		}
	}
}

int main() {
	int count = 0;
	scanf("%d%d",&M,&N);
	for(int i=0; i<N; i++) {
		for(int j=0; j<M; j++) {
			scanf("%d",&map[i][j]);
			if(map[i][j] == 1) {
				count++; q.push(p(i,j));
				check[i][j] = 1;
			}
		}
	}

	if(count == N*M) {printf("0"); return 0;}
	BFS();
	for(int i=0; i<N; i++) {
		for(int j=0; j<M; j++) {
			if(map[i][j] == 0) {
				printf("-1"); return 0;
			}
		}
	} printf("%d",days-1);
}