#include <iostream>
#include <vector>
#include <queue>
using namespace std;

typedef pair<int, int> P;

int main()
{
	int n, m; cin >> n >> m;
	vector< vector<P> > graph(n + 1, vector<P>());

	for (int i = 0; i < n - 1; i++)
	{
		int a, b, c; cin >> a >> b >> c;
		graph[a].emplace_back(P(b, c));
		graph[b].emplace_back(P(a, c));
	}

	for (int i = 0; i < m; i++)
	{
		int s, e; cin >> s >> e;

		queue< P > q;
		vector<int> dist(n + 1, -1);

		q.push(P(s, 0));

		while (!q.empty())
		{
			auto [curr, acc] = q.front(); q.pop();
			dist[curr] = acc;

			for (auto& [next, nextCost] : graph[curr])
			{
				if (dist[next] == -1)
					q.push(P(next, acc + nextCost));
			}
		}

		cout << dist[e] << '\n';
	}
}