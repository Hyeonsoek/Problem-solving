#include <iostream>
#include <vector>
#include <map>
using namespace std;

typedef vector<int> Vec;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	for (int n, m; cin >> n >> m;)
	{
		if (n == 0 && m == 0)
			break;

		Vec nodes(n);
		Vec height(n);
		Vec parent(n);
		vector<Vec> tree(n);
		
		int t = -1;
		for (int i = 0, v; i < n; i++)
		{
			cin >> v;
			nodes[i] = v;

			if (v == m) t = i;
		}

		height[1] = 1;
		parent[1] = 0;
		tree[0].emplace_back(1);

		for (int i = 2, r = 0; i < n; i++)
		{
			if (nodes[i - 1] + 1 != nodes[i])
			{
				r++;
			}
			height[i] = height[r] + 1;
			parent[i] = r;
			tree[r].emplace_back(i);
		}

		int pt = parent[t];
		int ans = 0;
		for (int i = 0; i < n; i++)
		{
			int p = parent[i];
			if (height[i] == height[t] && p != pt && parent[p] == parent[pt])
				ans++;
		}

		cout << ans << '\n';
	}
}