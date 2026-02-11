#include <bits/stdc++.h>
using namespace std;
constexpr int MIN = -1e9;

int n, m;
int board[1'001][1'001];
int cache[1'001][1'001];

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> n >> m;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			cin >> board[i][j];

	cache[n - 1][m - 1] = board[n - 1][m - 1];
	for (int i = m - 2; i >= 0; i--)
		cache[n - 1][i] = cache[n - 1][i + 1] + board[n - 1][i];

	for (int i = n - 2; i > 0; i--)
	{
		vector<int> left(m, MIN);
		vector<int> right(m, MIN);

		left[m - 1] = cache[i + 1][m - 1] + board[i][m - 1];
		for (int j = m - 2; j >= 0; j--)
			left[j] = board[i][j] + max(left[j + 1], cache[i + 1][j]);

		right[0] = cache[i + 1][0] + board[i][0];
		for (int j = 1; j < m; j++)
			right[j] = board[i][j] + max(right[j - 1], cache[i + 1][j]);

		for (int j = 0; j < m; j++)
			cache[i][j] = max(left[j], right[j]);
	}

	if (n > 1)
	{
		cache[0][m - 1] = board[0][m - 1] + cache[1][m - 1];
		for (int i = m - 2; i >= 0; i--)
			cache[0][i] = board[0][i] + max(cache[1][i], cache[0][i + 1]);
	}

	cout << cache[0][0];
}