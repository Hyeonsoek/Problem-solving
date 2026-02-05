#include <bits/stdc++.h>
using namespace std;

int n, k;

int main() {
	ios_base::sync_with_stdio(false);
	cout.tie(NULL);

	cin >> n >> k; n--;

	int next = 2;
	for(int j = 0; j < k; j++, n--)
		cout << 1 << ' ' << next++ << '\n';

	for(int i = 2; n; i++)
	{
		for (int j = 0; j < k - 1 && n; j++,n--)
			cout << i << ' ' << next++ << '\n';
	}
}