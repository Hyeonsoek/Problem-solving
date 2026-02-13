#include <bits/stdc++.h>
using namespace std;
constexpr int MAX = 101;

int a, n;
int cost[] = {6, 2, 5, 5, 4, 5, 6, 3, 7, 6};

long long cache[MAX] = {0, 0, 1, 7, 4, 2, 6, 8};

string getMax(int v)
{
	string s = v & 1 ? "7" : "";
	if (v & 1)
		v -= 3;

	for (int i = 0; i < v; i += 2)
		s += "1";

	return s;
}

int main()
{
	for (int i = 8; i < MAX; i++)
		cache[i] = 1LL << 60;

	for (int i = 2; i < MAX; i++)
		for (int j = 0; j < 10; j++)
			if (i + cost[j] < MAX)
				cache[i + cost[j]] = min(cache[i + cost[j]], cache[i] * 10 + j);

	cin >> n;
	while (n--)
	{
		cin >> a;
		cout << cache[a] << ' ' << getMax(a) << '\n';
	}
}