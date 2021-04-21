#include <cstdio>
#include <queue>
#include <vector>
using namespace std;
typedef pair<int,int> p;
vector< p > v;
int N,M,dir[4][2] = {{1,0},{0,1},{-1,0},{0,-1}},check[1001][1001];
char map[1001][1001];

void BFS(p start) {
	check[start.first][start.second] = 1;
	queue< p > q;
	q.push(start);
	while(!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		if (x == N-1) {break;}
		q.pop();
		for(int i=0; i<4; i++) {
			int xx = x + dir[i][0];
			int yy = y + dir[i][1];
			if(xx >= 0 && xx < N && yy >= 0 && yy < M && !check[xx][yy] && map[xx][yy] != '1') {
				q.push(p(xx,yy));
				check[xx][yy] = 1;
			}
		}
	}
}


int main() {
	scanf("%d%d",&N,&M);
	for(int i=0; i<N; i++) {
		scanf("%s",map[i]);
	}

	for(int i=0; i<M; i++) {
		if(map[0][i] == '0')
			v.push_back(p(0,i));
	}

	int size = v.size(),cnt=0;
	for(int i=0; i<size; i++)
		BFS(v[i]);
	for(int i=0; i<M; i++) {
		if(check[N-1][i] == 1) {
			printf("YES");
			return 0;
		} else cnt = 1;
	} if(cnt == 1) printf("NO");
}
