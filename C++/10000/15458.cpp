#include <iostream>
#include <vector>
#include <cstring>
constexpr auto MAX_N = 100'001;
constexpr auto MOD = 1'000'000'007;
using namespace std;

int n, k;
long cache[MAX_N][4];

vector<int> color(MAX_N, 0);
vector<bool> isVisited(MAX_N, false);

vector<vector<int>> graph(MAX_N);

long dynamic(int node, int p, int c)
{
	long& ret = cache[node][c];
	if (ret != -1)
		return ret;

	ret = 1;
	for (auto next : graph[node])
	{
		if (next == p)
			continue;

		if (c == color[next])
			return ret = 0;

		if (color[next])
		{
			ret = ret * dynamic(next, node, color[next]) % MOD;
		}
		else
		{
			long v = 0;
			for (int i = 1; i < 4; i++)
			{
				if (i != c) v += dynamic(next, node, i);
			}
			ret = ret * v % MOD;
		}
	}
	return ret;
}

//void dfs(int node, int p)
//{
//	for (auto next : graph[node])
//	{
//		if (p == next) continue;
//		dfs(next, node);
//	}
//
//	if (color[node])
//	{
//		cache[node][color[node]] = 1;
//	}
//	else
//	{
//		for (int i = 1; i < 4; i++)
//			cache[node][i] = 1;
//	}
//
//	for (auto next : graph[node])
//	{
//		if (p == next) continue;
//		cache[node][1] *= cache[next][2] + cache[next][3];
//		cache[node][2] *= cache[next][1] + cache[next][3];
//		cache[node][3] *= cache[next][1] + cache[next][2];
//
//		for (int i = 1; i < 4; i++)
//			cache[node][i] %= MOD;
//	}
//
//	cout << "cache[" << node << "][" << p << "][" << c << "] = " << ret << '\n';
//}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	memset(cache, -1, sizeof(cache));

	cin >> n >> k;

	for (int i = 0; i < n - 1; i++)
	{
		int u, v; cin >> u >> v;
		graph[u].emplace_back(v);
		graph[v].emplace_back(u);
	}

	for (int i = 0; i < k; i++)
	{
		int u, c; cin >> u >> c;
		color[u] = c;
	}


	if (color[1] == 0)
	{
		long answer = 0;
		for (int i = 1; i < 4; i++)
		{
			answer += dynamic(1, 0, i);
			answer %= MOD;
		}

		cout << answer << '\n';
	}
	else
	{
		cout << dynamic(1, 0, color[1]);
	}
}