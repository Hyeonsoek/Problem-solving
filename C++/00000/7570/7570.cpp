#include <bits/stdc++.h>
using namespace std;

int n;
int cache[1'000'001];

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> n;
	for (int a, i = 0; i < n; i++)
	{
		cin >> a;
		cache[a] = cache[a - 1] + 1;
	}

	int res = 0;
	for (int i = 1; i <= n; i++)
		res = max(res, cache[i]);

	cout << n - res;
}