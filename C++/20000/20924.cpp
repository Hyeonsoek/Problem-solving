#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

typedef pair<int, int> P;

int n, r;
vector<P> graph[200'001];
vector<P> tree[200'001];

void dfs(int node, int prev)
{
	for (auto [next, d] : graph[node])
	{
		if (next != prev)
		{
			dfs(next, node);
			tree[node].emplace_back(P(next, d));
		}
	}
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> n >> r;

	for (int i = 1, a, b, d; i < n; i++)
	{
		cin >> a >> b >> d;

		graph[a].emplace_back(P(b, d));
		graph[b].emplace_back(P(a, d));
	}

	dfs(r, 0);

	int m = r, column = 0;
	while(tree[m].size() == 1)
	{
		auto [next, d] = tree[m][0];
		m = next; column += d;
	}

	int branch = 0;
	queue<P> q;
	q.push(P(m, 0));

	while (!q.empty())
	{
		auto [node, dist] = q.front(); q.pop();
		branch = max(branch, dist);

		for (auto [next, d] : tree[node])
		{
			q.push(P(next, dist + d));
		}
	}

	cout << column << ' ' << branch;
}