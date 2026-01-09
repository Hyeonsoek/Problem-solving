#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;
typedef vector< vector<int> > Graph;

Graph graph;
vector<bool> isVisited;

int dfs(int node)
{
	isVisited[node] = true;

	int c = 0;
	for (auto next : graph[node])
	{
		if (isVisited[next] == false)
			c += dfs(next);
	}

	return c == 0 ? 1 : c;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int n, w; cin >> n >> w;

	graph.assign(n + 1, vector<int>());
	isVisited.assign(n + 1, false);

	for (int i = 0; i < n - 1; i++)
	{
		int u, v; cin >> u >> v;
		graph[u].emplace_back(v);
		graph[v].emplace_back(u);
	}

	cout << setprecision(10) << (double) w / dfs(1);
}