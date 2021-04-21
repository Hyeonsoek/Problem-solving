#include <cstdio>
#include <queue>
#include <vector>
#include <utility>
#define INF (1<<31)-1
using namespace std;


typedef pair<int,int> p;
int V,E,start,end;
priority_queue<p,vector<p>,greater<p> > pq;
vector< p > map[1001];
int dist[1001];

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
	scanf("%d%d",&V,&E);
	for(int i=1; i<=V; i++) map[i].push_back(p(0,0));
	for(int i=0; i<E; i++){
		int u,v,w;
		scanf("%d%d%d",&u,&v,&w);
		map[u].push_back(p(v,w));
	}
	scanf("%d%d",&start,&end);
	dijikstra();
	printf("%d\n",dist[end]);
}
