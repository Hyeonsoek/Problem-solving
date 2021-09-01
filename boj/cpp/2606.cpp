#include <cstdio>
#include <queue>
using namespace std;
int map[101][101],check[101],N,K,count;
void bfs() {
	queue<int> q;
	q.push(1);
	check[1]=1;
	while(!q.empty()) {
		int x = q.front();
		count++;
		q.pop();
		for (int i=1; i<=N; i++) {
			if (map[x][i] && check[i]==0) {
				q.push(i);
				check[i]=check[x]+1;
			}
		}
	} printf("%d",count-1);
}
int main() {
	scanf("%d",&N);
	for(scanf("%d",&K);K--;) {
		int x,y;
		scanf("%d%d",&x,&y);
		map[x][y] = map[y][x] = 1;
	} bfs();
}
