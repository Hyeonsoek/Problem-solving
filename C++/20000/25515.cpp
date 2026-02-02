#include <iostream>
#include <vector>
using namespace std;

int n;
int value[100'000];
vector<int> tree[100'000];

long dfs(int node)
{
	long val = value[node];
	for (auto next : tree[node])
	{
		long v = dfs(next);
		if (v > 0)
			val += v;
	}
	return val;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> n;
	for (int p, c, i = 1; i < n; i++)
	{
		cin >> p >> c;
		tree[p].emplace_back(c);
	}

	for (int i = 0; i < n; i++)
		cin >> value[i];

	cout << dfs(0);
}