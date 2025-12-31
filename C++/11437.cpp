#include <iostream>
#include <vector>
constexpr auto MAX_DEPTH = 18;
constexpr auto ROOT = 1;
using namespace std;

typedef vector< vector<int> > maxtrix;

int n, m;
vector<int> depth;
maxtrix graph;
maxtrix parent;

void dfs(int node)
{
	for (auto& next : graph[node])
	{
		if (!depth[next])
		{
			depth[next] = depth[node] + 1;
			parent[next][0] = node;
			dfs(next);
		}
	}
}

int lca(int u, int v)
{
	if (depth[u] < depth[v])
		swap(u, v);

	for (int pow = MAX_DEPTH - 1; pow >= 0; pow--)
	{
		if (depth[u] - depth[v] >= (1 << pow))
		{
			u = parent[u][pow];
		}
	}

	if (u != v)
	{
		for (int pow = MAX_DEPTH - 1; pow >= 0; pow--)
		{
			if (parent[u][pow] && parent[u][pow] != parent[v][pow])
			{
				u = parent[u][pow];
				v = parent[v][pow];
			}
		}

		if (u != v)
		{
			u = parent[u][0];
			v = parent[v][0];
		}
	}
	return u;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> n;

	n++;
	depth.assign(n, 0);
	graph.assign(n, vector<int>(MAX_DEPTH, 0));
	parent.assign(n, vector<int>(MAX_DEPTH, 0));
	n--;

	for (int i = 1; i < n; i++)
	{
		int a, b;  cin >> a >> b;
		graph[a].emplace_back(b);
		graph[b].emplace_back(a);
	}

	depth[ROOT] = 1;
	dfs(ROOT);

	for (int pow = 1; pow < MAX_DEPTH; pow++)
	{
		for (int node = 1; node <= n; node++)
		{
			auto& prev = parent[node][pow - 1];
			if (prev)
			{
				parent[node][pow] = parent[prev][pow - 1];
			}
		}
	}

	cin >> m;

	while (m--)
	{
		int u, v; cin >> u >> v;
		cout << lca(u, v) << "\n";
	}
}