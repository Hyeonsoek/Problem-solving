#include <iostream>
#include <vector>
#include <functional>
using namespace std;

bool solve()
{
	int n, m; cin >> n >> m;
	
	vector<bool> isVisited(n+1);
	vector<vector<int>> graph(n+1);

	for (int i = 0, a, b; i < m; i++)
	{
		cin >> a >> b;
		graph[a].emplace_back(b);
		graph[b].emplace_back(a);
	}

	function<bool(int, int)> dfs = [&](int node, int prev) {
		isVisited[node] = true;
		for (auto next : graph[node])
		{
			if (next != prev)
			{
				if (isVisited[next] || !dfs(next, node))
					return false;
			}
		}

		return true;
	};

	if (!dfs(1, 0))
		return false;

	for (int i = 1; i <= n; i++)
		if (!isVisited[i])
			return false;

	return true;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int t; cin >> t;
	while (t--)
	{
		cout << (solve() ? "tree" : "graph") << "\n";
	}
}