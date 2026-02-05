#include <bits/stdc++.h>
using namespace std;
constexpr int MAX = 1001;

int n, q;
int arr[MAX];
vector<int> graph[MAX];

void BFS(int u, int v)
{
	vector<int> parent(n + 1);
	queue<int> queue;

	queue.push(u);
	parent[u] = -1;

	while (!queue.empty())
	{
		int node = queue.front(); queue.pop();
		for(auto next : graph[node])
		{
			if (parent[next] == 0)
			{
				parent[next] = node;
				queue.push(next);
			}
		}
	}

	int j = -1;
	for(int p = v; p != -1; j++, p=parent[p]);

	for(int p = v; p != -1; j--, p=parent[p])
		arr[p] += j;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> n;
	for (int a, b, i = 1; i < n; i++)
	{
		cin >> a >> b;
		graph[a].emplace_back(b);
		graph[b].emplace_back(a);
	}

	cin >> q;
	for (int query, i = 0; i < q; i++)
	{
		cin >> query;

		if (query == 1)
		{
			int u, v;
			cin >> u >> v;
			BFS(u, v);
		}
		else
		{
			int x; cin >> x;
			cout << arr[x] << '\n';
		}
	}
}