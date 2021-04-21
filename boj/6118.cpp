#include <cstdio>
#include <queue>
#include <vector>
#include <utility>
#include <algorithm>
#define INF 60000
#define MAX_V 20001
using namespace std;
typedef pair<int,int> PAIR;

int N,M;
vector<PAIR> map[MAX_V];
vector<int> dist(MAX_V,INF);
priority_queue< PAIR > pq;

void dijkstra() {
	dist[1] = 0;
	pq.push(make_pair(0,1));
	while(!pq.empty()) {
		int cost = -pq.top().first;
		int here = pq.top().second;
		pq.pop();
		int len = map[here].size();
		for(int i=0; i<len; ++i) {
			int there = map[here][i].first;
			int newcost = map[here][i].second + cost;
			if(dist[there] > newcost) {
				dist[there] = newcost;
				pq.push(make_pair(-newcost,there));
			}
		}
	}
}

int main() {
	scanf("%d%d",&N,&M);
	for(int i=0; i<M; ++i) {
		int u,v;
		scanf("%d%d",&u,&v);
		map[u].push_back(make_pair(v,1));
		map[v].push_back(make_pair(u,1));
	}

	dijkstra();

	int max=-INF,count=0;
	vector<int> num;

	for(int i=1; i<=N; ++i)
		if(max < dist[i] && dist[i] != INF)
			max = dist[i];
	for(int i=1; i<=N; ++i)
		if(max == dist[i]) {
			count++;
			num.push_back(i);
		}
	sort(num.begin(),num.end());
	printf("%d %d %d",num[0],max,count);
}