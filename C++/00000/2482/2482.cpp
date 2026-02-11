#include <bits/stdc++.h>
using namespace std;
constexpr int MOD = 1e9 + 3;

int n, k;
int cache[1001][1001];

int main()
{
	cin >> n >> k;

	for (int i = 0; i <= n; i++)
		cache[i][0] = 1;
	cache[1][1] = 1;

	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= (i / 2); j++)
			cache[i][j] = (cache[i - 2][j - 1] + cache[i - 1][j]) % MOD;

	cout << cache[n][k];
}