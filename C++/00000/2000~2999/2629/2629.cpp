#include <bits/stdc++.h>
using namespace std;
constexpr int MAX_VAL = 40001;

int n, q;
int arr[31];
bool cache[31][MAX_VAL];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> n;
	for(int i = 0; i < n; i++)
	{
		cin >> arr[i];
		cache[i][0] = true;
	}
	
	cache[0][arr[0]] = true;
	for(int i = 1; i < n; i++)
	{
		cache[i][arr[i]] = true;
		for (int j = 1; j < MAX_VAL; j++)
		{
			if (cache[i - 1][j])
			{
				cache[i][j] = true;
				if (j + arr[i] < MAX_VAL)
					cache[i][j + arr[i]] = true;
				
				int t = abs(j - arr[i]);
				if (t < MAX_VAL)
					cache[i][t] = true;
			}
		}
	}

	auto validate = [&](int val) {

		for(int i = 0; i < n; i++)
			if (cache[i][val])
				return true;
		return false;
	};

	cin >> q;
	while (q--)
	{
		int val; cin >> val;
		cout << (validate(val) ? "Y" : "N") << ' ';
	}
}