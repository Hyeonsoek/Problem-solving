#include <iostream>
#include <cstring>
const int MAX = 100'001;
using namespace std;

int n, m;
int parent[MAX];

int find(int u)
{
	return parent[u] < 0 ? u : parent[u] = find(parent[u]);
}

void merge(int u, int v)
{
	u = find(u), v = find(v);
	if (u != v) parent[v] = u;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> n >> m;

	memset(parent, -1, sizeof(parent));

	for (int i = 0, u, v; i < m; i++)
	{
		cin >> u >> v;
		merge(u, v);
	}

	int res = 0;
	for (int i = 1; i <= n; i++)
		if (parent[i] < 0)
			res++;

	cout << m - n - 1 + 2 * res;
}