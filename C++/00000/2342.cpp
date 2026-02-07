#include <bits/stdc++.h>
using namespace std;
constexpr int MAX = 100'001;

int cost[5][5] = {
	{1, 2, 2, 2, 2},
	{2, 1, 3, 4, 3},
	{2, 3, 1, 3, 4},
	{2, 4, 3, 1, 3},
	{2, 3, 4, 3, 1}
};

int n;
int arr[MAX];
int cache[MAX][5][5];

int dynamic(int i, int l, int r)
{
	if (i == n)
		return 0;

	int &ret = cache[i][l][r];
	if (ret != -1)
		return ret;

	return ret = min(
		dynamic(i + 1, arr[i], r) + cost[l][arr[i]],
		dynamic(i + 1, l, arr[i]) + cost[r][arr[i]]
	);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	memset(cache, -1, sizeof(cache));

	for(int i = 0; cin >> arr[i] && arr[i] != 0; i++, n++);

	cout << dynamic(0, 0, 0);
}