#include <cstdio>
#include <queue>
using namespace std;

int V,E,count,map[1001][1001],check[1001];
int dir[4][2] = {{1,0},{-1,0},{0,-1},{0,1}};

void bfs(int x,int y) {
	queue<int> q;
	q.push(x);
	check[x] = 1;
	while(!q.empty()) {
		int x = q.front();
		q.pop();
		for(int i=1; i<=V; i++) {
			if(map[x][i] && !check[i]) {
				q.push(i);
				check[i] = 1;
			}
		}
	}
}

int main() {
	scanf("%d%d",&V,&E);
	for(int i=0; i<E; i++) {
		int v1,v2;
		scanf("%d%d",&v1,&v2);
		map[v1][v2] = map[v2][v1] = 1;
	}

	for(int i=1; i<=V; i++) {
		for(int j=1; j<=V; j++) {
			if(map[i][j] && !check[i]) {
				bfs(i,j); count++;
			}
		}
	}
	
	for(int i=1; i<=V; i++) {
		if(!check[i]) {
			int newcheck = 1;
			for(int j=1; j<=V; j++) {
				if(map[i][j]) {
					newcheck = 0; break;
				}
			} if(newcheck) count++;
		}
	}
	
	printf("%d",count);
}
