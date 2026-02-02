#include <iostream>
#include <vector>
using namespace std;
typedef pair<int, int> P;

int k;
int n;
vector<int> v;

P dfs(int node)
{
	if (node * 2 > n)
		return P(0, 0);

	int l = node << 1;
	int r = node << 1 | 1;

	P L = dfs(l);
	P R = dfs(r);

	int depth_l = L.second + v[l];
	int depth_r = R.second + v[r];

	int difDepth = abs(depth_l - depth_r);
	int maxDepth = max(depth_l, depth_r);

	return P(L.first + R.first + v[l] + v[r] + difDepth, maxDepth);
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	v.emplace_back(0);
	v.emplace_back(0);

	cin >> k;
	n = (1 << (k + 1)) - 1;
	for (int i = 1; i < n; i++)
	{
		int w; cin >> w;
		v.emplace_back(w);
	}

	cout << dfs(1).first << '\n';
}