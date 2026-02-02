#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long LL;

int n;
vector< LL > counts;
vector< vector<int> > graph;
vector<bool> isVisited;

LL dfs(int node)
{
	isVisited[node] = true;

	LL value = counts[node];
	for (auto next : graph[node])
	{
		if (isVisited[next] == false)
		{
			value += dfs(next);
		}
	}

	return max(0LL, value);
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> n;

	counts.assign(n + 1, 0);
	graph.assign(n + 1, vector<int>());
	isVisited.assign(n + 1, false);

	for (int i = 2; i <= n; i++)
	{
		char t;
		int a, p;
		cin >> t >> a >> p;

		if (t == 'W')
			a *= -1;

		counts[i] += a;

		graph[p].emplace_back(i);
		graph[i].emplace_back(p);
	}

	cout << dfs(1) << '\n';
}