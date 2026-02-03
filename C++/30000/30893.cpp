#include <bits/stdc++.h>
using namespace std;
constexpr int MAX = 100'001;

int n, u, v;
bool visited[MAX];
vector<int> graph[MAX];

bool DFS(int node, bool isSec)
{
	visited[node] = true;

	if (node == v)
		return true;

	int cnt = 0;
	bool res = isSec;
	for(auto next : graph[node])
	{
		if (visited[next] == false)
		{
			cnt++;
			if (isSec) res &= DFS(next, false);
			else res |= DFS(next, true);
		}
	}

	if (cnt == 0 && res)
		return false;

	return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> u >> v;
    for(int a, b, i = 1; i < n; i++)
    {
        cin >> a >> b;
        graph[a].emplace_back(b);
        graph[b].emplace_back(a);
    }

	cout << (DFS(u, false) ? "First" : "Second") << '\n';
}