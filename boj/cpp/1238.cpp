#include <cstdio>
#include <queue>
#include <vector>
#include <utility>
#define INF (1<<31)-1
using namespace std;


typedef pair<int,int> p;
int V,E,end,maxx;
vector< p > map[1001];
int dist[1001];

void dijikstra()
{
	priority_queue<p,vector<p>,greater<p> > pq;
	for(int i=1; i<=V; i++) dist[i] = INF;
	dist[end] = 0;
	pq.push(p(0,end));
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

int rdijikstra(int start)
{
	int dist[1001] = {};
	priority_queue<p,vector<p>,greater<p> > pq;
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
	} return dist[end];
}

int main()
{
	scanf("%d%d%d",&V,&E,&end);
	for(int i=1; i<=V; i++) map[i].push_back(p(0,0));
	for(int i=0; i<E; i++){
		int u,v,w;
		scanf("%d%d%d",&u,&v,&w);
		map[u].push_back(p(v,w));
	}
	dijikstra();
	for(int i=1; i<=V; i++) {
		int re = rdijikstra(i);
		if((re + dist[i]) > maxx) {
			maxx = re + dist[i];
		}
	}
	printf("%d",maxx);
}
