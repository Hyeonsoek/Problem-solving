#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef pair<int, int> P;

int ans;
bool isVisited[10'001];
vector<P> graph[10'001];

void dfs(int node, int dist)
{
	ans = max(dist, ans);
	isVisited[node] = true;
	for (auto [next, d] : graph[node])
	{
		if (isVisited[next] == false)
			dfs(next, dist + d);
	}
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	for (int a, b, c; cin >> a >> b >> c;)
	{
		graph[a].emplace_back(P(b, c));
		graph[b].emplace_back(P(a, c));
	}

	for (int i = 1; i < 10001; i++)
	{
		dfs(i, 0);
		memset(isVisited, false, sizeof(isVisited));
	}

	cout << ans;
}