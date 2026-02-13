#include <bits/stdc++.h>
using namespace std;
constexpr int MAX = 30'001;

int n, m, k;
int arr[MAX];
int parent[MAX];
int cnt[MAX];

int find(int u)
{
	if (u == parent[u])
		return u;
	return parent[u] = find(parent[u]);
}

void merge(int u, int v)
{
	u = find(u);
	v = find(v);

	if (u == v)
		return;

	if (arr[u] < arr[v])
		swap(u, v);

	parent[v] = u;
	arr[u] += arr[v];
	cnt[u] += cnt[v];
}

void dynamic()
{
	int r, c, s;
	int cache[k] = {};

	for (int i = 1; i <= n; i++)
	{
		if (i != find(i))
			continue;

		r = find(i);
		c = cnt[r];
		s = arr[r];
		for (int j = k - 1; j >= c; j--)
			cache[j] = max(cache[j], cache[j - c] + s);
	}

	cout << cache[k - 1];
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	cin >> n >> m >> k;
	for (int i = 1; i <= n; i++)
	{
		cin >> arr[i];
		cnt[i] = 1;
		parent[i] = i;
	}

	for (int a, b, i = 0; i < m; i++)
	{
		cin >> a >> b;
		merge(a, b);
	}

	dynamic();
}