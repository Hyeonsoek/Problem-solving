#include <algorithm>
#include <iostream>
#include <vector>
#include <tuple>
using namespace std;

int n, p;
vector<int> parent;
vector<int> cost;
vector<tuple<int, int, int> > edges;

int find(int x)
{
	if (parent[x] == x)
		return x;
	return parent[x] = find(parent[x]);
}

bool merge(int u, int v)
{
	u = find(u);
	v = find(v);

	if (u == v)
		return false;

	parent[u] = v;
	return true;
}

int main()
{
	cin.tie(0); cout.tie(0);
	ios_base::sync_with_stdio(false);

	cin >> n >> p;

	int result = 1000;

	cost.emplace_back(0);
	for (int i = 0; i < n; i++)
	{
		int c;
		cin >> c;
		result = min(result, c);
		cost.emplace_back(c);
	}

	for (int i = 0; i < p; i++)
	{
		int s, e, c;
		cin >> s >> e >> c;
		edges.emplace_back(make_tuple(c * 2 + cost[s] + cost[e], s, e));
	}

	sort(edges.begin(), edges.end());

	for (int i = 0; i <= n; i++)
		parent.emplace_back(i);

	for (int i = 0; i < p; i++)
	{
		int c, s, e;
		tie(c, s, e) = edges[i];
		
		if (merge(s, e))
		{
			result += c;
		}
	}

	cout << result << '\n';
}