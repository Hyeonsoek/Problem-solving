#include <cstdio>
#include <queue>
#include <utility>
#include <vector>
#define INF (1<<31)-1
using namespace std;
typedef pair<int,int> p;
vector<p> map[101];
int dist[101][101],N,M;

void dijikstra(int i) {
	for(int j=1; j<=N; j++) dist[i][j] = INF;
	dist[i][i] = 0;
	priority_queue<p,vector<p>,greater<p> > pq;
	pq.push(p(0,i));
	while(!pq.empty()) {
		int cost = pq.top().first;
		int pos = pq.top().second;
		pq.pop();
		int len = map[pos].size();
		for(int j=0; j<len; j++) {
			int newcost = map[pos][j].second;
			int ppos = map[pos][j].first;
			if(dist[i][ppos] > newcost + cost) {
				dist[i][ppos] = newcost + cost;
				pq.push(p(dist[i][ppos],ppos));
			}
		}
	}
}

int main() {
	scanf("%d%d",&N,&M);
	for(int i=0; i<M; i++) {
		int x,y,z;
		scanf("%d%d%d",&x,&y,&z);
		map[x].push_back(p(y,z));
	}

	for(int i=1; i<=N; i++) {
		dijikstra(i);
		for(int j=1; j<=N; j++) {
			printf("%d ",dist[i][j]);
		} printf("\n");
	}
}