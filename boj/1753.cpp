#include <cstdio>
#include <queue>
#include <vector>
#include <utility>
#define INF (1<<30)-1
using namespace std;


typedef pair<int,int> p;
int V,E,start;
priority_queue<p,vector<p>,greater<p> > pq;
vector< p > map[20001];
int dist[20001];

void dijikstra()
{
	for(int i=1; i<=V; i++) dist[i] = INF;
	dist[start] = 0;
	pq.push(p(0,start));
	while(!pq.empty()) {
		int cost = pq.top().first;
		int pos = pq.top().second;
		pq.pop();
		int len = map[pos].size();
		for(int i=0; i<len; i++) {
			int ppos = map[pos][i].first;
			int newcost = map[pos][i].second;
			if(dist[ppos] > newcost + cost) {
				dist[ppos] = newcost + cost;
				pq.push(p(dist[ppos],ppos));
			}
		}
	}
}

int main()
{
	scanf("%d%d%d",&V,&E,&start);
	for(int i=1; i<=V; i++) map[i].push_back(p(0,0));
	for(int i=0; i<E; i++){
		int u,v,w;
		scanf("%d%d%d",&u,&v,&w);
		map[u].push_back(p(v,w));
	}
	dijikstra();
	for(int i=1; i<=V; i++) {
		if(dist[i] == INF) printf("INF\n");
		else printf("%d\n",dist[i]);
	}
}
