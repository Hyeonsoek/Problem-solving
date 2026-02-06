#include <bits/stdc++.h>
using namespace std;
constexpr int MAX = 1 << 12 + 1;

typedef tuple<int, int, int> T;

int d, n, u, t, cnt = 1;
bool banned[MAX];

int DFS(int node, int h)
{	
	cnt--;

	if (h >= d)
		return 0;

	int val = 0;
	if (!banned[node << 1])
	{
		val += u + DFS(node << 1, h + 1);
		if (cnt > 0) val += u;
	}
	
	if (!banned[node << 1 | 1])
	{
		val += u + DFS(node << 1 | 1, h + 1);
		if (cnt > 0) val += u;
	}

	return val;
}

int BFS()
{
	int res = 0, h = 1;
	queue<T> q;
	q.push(T(1, u, 0));

	while (h++ < d)
	{
		int size = q.size();
		bool branched = false;
		for (int i = 0; i < size; i++)
		{
			auto [node, cost, val] = q.front(); q.pop();

			int L = node << 1;
			int R = node << 1 | 1;

			if (!banned[L] && !banned[R])
				cost += t;

			val += cost;
			if (!banned[L] || !banned[R])
				res = max(res, val);

			if (!banned[L]) { q.push(T(L, cost, val)); cnt++; }
			if (!banned[R]) { q.push(T(R, cost, val)); cnt++; }
		} 
	}
	
	return res;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);

	cin >> d >> n >> u >> t;
	for(int s, e, i = 0; i < n; i++)
	{
		cin >> s >> e;
		banned[e] = true;
	}

	int p = BFS();
	int t = DFS(1, 1);

	if (t == p)
	{
		cout << ":blob_twintail_thinking:";
		return 0;
	}

	cout << ((t < p) ? ":blob_twintail_sad:" : ":blob_twintail_aww:");
}