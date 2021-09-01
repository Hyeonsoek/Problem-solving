#include <cstdio>
#include <queue>
using namespace std;
int map[101][101],input[101][101],N;
void bfs(int i,int j) {
	int check[101]={},count=0;
	queue<int> q;
	q.push(i);
	while (!q.empty()) {
		int x = q.front();
		count++;
		q.pop();
		if (x == j&&count>1) {map[i][j]=1;break;}
		for (int i=0;i<N;i++) {
			if (!check[i]&&input[x][i]==1) {
				check[i]=1;
				q.push(i);
			}
		}
	}
}
int main() {
	scanf("%d",&N);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			scanf("%d",&input[i][j]);
		}
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0;j < N; j++) {
			bfs(i,j);
			printf("%d ",map[i][j]);
		}
		printf("\n");
	}
}
