// #include <bits/stdc++.h>
// using namespace std;
// constexpr int MAX = 50'001;
// typedef pair<int, int> P;

// int n;
// vector<int> f[MAX];
// vector<int> tree[MAX];

// P DFS(int node)
// {
// 	int r = 0;
// 	vector<int> h;
// 	for(auto next : tree[node])
// 	{
// 		auto [rn, hn] = DFS(next);
// 		h.emplace_back(hn);
// 		r = max(r, rn);
// 	}

// 	if (h.size() == 0)
// 		return P(0, 0);
	
// 	if (h.size() == 1)
// 		return P(max(r, h[0] + 1), h[0] + 1);
	
// 	sort(h.begin(), h.end(), greater<int>());
// 	return P(max(r, h[0] + h[1] + 2), h[0] + 1);
// }

// int main() {
// 	ios_base::sync_with_stdio(false);
// 	cin.tie(NULL); cout.tie(NULL);

// 	cin >> n;
// 	f[0].emplace_back(0);
// 	int a, p = 0, node = 1;
// 	for (int i = 1; i <= n; i++)
// 	{
// 		cin >> a;
// 		for(int j = 0; j < a; j++)
// 		{
// 			f[i].emplace_back(node);
// 			int b = f[i-1][j % f[i-1].size()];
// 			tree[b].emplace_back(node++);
// 		}
// 		p = node - a;
// 	}

// 	cout << DFS(0).first << '\n';
// }

#include <bits/stdc++.h>
using namespace std;

int n;
int arr[51];

int main() {
	cin >> n;
	for (int i = 1; i <= n; i++)
		cin >> arr[i];

	int res = 0;
	for (int i = n, j = i; i >= 0; i--, j = i)
	{
		while (arr[j] > 1) j--;
		res = max(res, n + i - j * 2);
	}
	cout << res;
}