#include <bits/stdc++.h>
constexpr int MAX = 1001;
constexpr int MOD = 1e9 + 7;
using namespace std;

int n, q;
string arr[MAX];
vector<int> graph[MAX];

int BFS(int s, int e)
{	
	vector<int> dist(n + 1);
	vector<bool> visited(n + 1);

	queue<int> q;

	q.push(s);
	visited[s] = true;

	while (!q.empty())
	{
		int node = q.front(); q.pop();
		dist[node] = stoull(to_string(dist[node]) + arr[node]) % MOD;
		for(auto next : graph[node])
		{
			if (visited[next] == false)
			{
				visited[next] = true;
				dist[next] = dist[node];
				q.push(next);
			}
		}
	}

	return dist[e];
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> n >> q;
	for (int i = 1; i <= n; i++) cin >> arr[i];

	for (int a, b, i = 1; i < n; i++)
	{
		cin >> a >> b;
		graph[a].emplace_back(b);
		graph[b].emplace_back(a);
	}

	for(int x, y, i = 0; i < q; i++)
	{
		cin >> x >> y;
		cout << BFS(x, y) << '\n';
	}
}