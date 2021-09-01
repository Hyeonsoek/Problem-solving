#include <cstdio>
#include <queue>
#include <vector>
#include <utility>
#define INF (1<<31)-1;
using namespace std;
typedef pair<int,int> p;
typedef pair<p,int> np;
typedef vector<vector<int> > VEC;
struct cmp {
	bool operator()(np a, np b) {
		return (a.second > b.second);
	}
};
int dir[4][2] = {{1,0},{0,1},{-1,0},{0,-1}};

int dijikstra(VEC &map,int n) {
	priority_queue<np,vector<np>,cmp> pq;
	VEC dist(n,vector<int>(n));
	VEC check(n,vector<int>(n));
	for(int i=0; i<n; i++) {
		for(int j=0; j<n; j++) {
			dist[i][j] = INF;
		}
	}
	check[0][0] = 1;
	pq.push(np(p(0,0),map[0][0]));
	while(!pq.empty()) {
		int x = pq.top().first.first;
		int y = pq.top().first.second;
		int cost = pq.top().second;
		pq.pop();
		for(int i=0; i<4; i++) {
			int xx = x + dir[i][0];
			int yy = y + dir[i][1];
			if(xx >= 0 && xx < n && yy >= 0 && yy < n && !check[xx][yy]) {
				int ncost = cost + map[xx][yy];
				if(dist[xx][yy] > ncost) {
					dist[xx][yy] = ncost;
					check[xx][yy] = 1;
					pq.push(np(p(xx,yy),dist[xx][yy]));
				}
			}
		}
	} return dist[n-1][n-1];
}

int main() {
	int N;
	scanf("%d",&N);
	for(int i=1;N!=0;i++) {
		VEC map(N,vector<int>(N));
		for(int j=0; j<N; j++) {
			for(int k=0; k<N; k++) {
				scanf("%d",&map[j][k]);
			}
		} printf("Problem %d: %d\n",i,dijikstra(map,N));
		scanf("%d",&N);
	}
}
