#include <iostream>
#include <vector>
using namespace std;

typedef vector< vector<int> > graph;

graph tree;
vector<int> parent;
vector<int> depth;

void dfs(int node)
{
	for (auto next : tree[node])
	{
		if (!depth[next])
		{
			depth[next] = depth[node] + 1;
			dfs(next);
		}
	}
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	int t; cin >> t;

	while (t--)
	{
		int n; cin >> n;

		depth.assign(n + 1, 0);
		parent.assign(n + 1, 0);
		tree.assign(n + 1, vector<int>());

		for (int i = 1; i < n; i++)
		{
			int a, b; cin >> a >> b;
			tree[a].emplace_back(b);
			parent[b] = a;
		}

		for (int i = 1; i <= n; i++)
		{
			if (parent[i] == 0)
			{
				depth[i] = 1;
				dfs(i);
			}
		}

		int s, e; cin >> s >> e;

		if (depth[s] < depth[e])
			swap(s, e);

		while (depth[s] > depth[e])
		{
			s = parent[s];
		}

		while (s != e)
		{
			s = parent[s];
			e = parent[e];
		}

		cout << s << '\n';
	}
}
