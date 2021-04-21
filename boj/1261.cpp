#include <cstdio>
#include <queue>
#include <vector>
#include <utility>
#define INF (1<<31)-1;
using namespace std;
typedef pair<int,int> p;
typedef pair<p,int> np;
typedef vector<vector<int> > VEC;
char map[101][101];
int n,m;
struct cmp {
	bool operator()(np a, np b) {
		return (a.second > b.second);
	}
};
int dir[4][2] = {{1,0},{0,1},{-1,0},{0,-1}};

int dijikstra() {
	priority_queue<np,vector<np>,cmp> pq;
	VEC dist(n,vector<int>(m));
	VEC check(n,vector<int>(m));
	for(int i=0; i<n; i++) {
		for(int j=0; j<m; j++) {
			dist[i][j] = INF;
		}
	}
	check[0][0] = 1;
	dist[0][0] = 0;
	pq.push(np(p(0,0),map[0][0]-'0'));
	while(!pq.empty()) {
		int	y = pq.top().first.first;
		int x = pq.top().first.second;
		int cost = pq.top().second;
		pq.pop();
		for(int i=0; i<4; i++) {
			int yy = y + dir[i][0];
			int xx = x + dir[i][1];
			if(xx >= 0 && xx < m && yy >= 0 && yy < n && !check[yy][xx]) {
				int ncost = cost + (map[yy][xx]-'0');
				if(dist[yy][xx] > ncost) {
					dist[yy][xx] = ncost;
					check[yy][xx] = 1;
					pq.push(np(p(yy,xx),dist[yy][xx]));
				}
			}
		}
	} return dist[n-1][m-1];
}

int main() {
	scanf("%d%d",&m,&n);
	for(int i=0; i<n; i++) {
		scanf("%s",map[i]);
	}

	printf("%d",dijikstra());
}