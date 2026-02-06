#include <bits/stdc++.h>
using namespace std;

int k;

int main() {
	ios_base::sync_with_stdio(false);
	cout.tie(NULL);

	cin >> k;

	int a;
	for(int i = 1; i <= sqrt(k); i++)
		if (k % i == 0)
			a = i;

	int b = k / a;
	cout << a + b << '\n';
	for(int i = 1; i <= b; i++)
		cout << i << ' ' << i + 1 << '\n';
	
	for(int i = 1; i < a; i++)
		cout << i << ' ' << i + b + 1 << '\n';
}