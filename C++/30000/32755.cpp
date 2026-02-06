#include <bits/stdc++.h>
using namespace std;

int n;
int degree[501];

int main()
{
	cin >> n;
	for (int u, v, i = 1; i < n; i++)
	{
		cin >> u >> v;
		degree[u]++;
		degree[v]++;
	}

	for (int i = 1; i <= n; i++)
	{
		if (degree[i] == n - 1)
		{
			cout << n - 1;
			return 0;
		}
	}

	cout << n;
}