#include <bits/stdc++.h>
using namespace std;
constexpr int MAX_V = 1e9 + 1;
constexpr int MAX = 1e5 + 1;
typedef pair<int, int> P;

int n, s;
int w[MAX];
bool visited[MAX];
P edge[MAX];

vector<int> cache;
vector<P> graph[MAX];

int dynamic(int node)
{
	visited[node] = true;

	int ts = w[node];
	for(auto [next, e] : graph[node])
	{
		if (visited[next] == false)
		{
			int nexts = dynamic(next);
			
			ts += nexts;
			cache[e] = min(cache[e], abs(s - 2 * nexts));
		}
	}

	return ts;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> n;
	for(int a, b, i = 1; i < n; i++)
	{
		cin >> a >> b;
		edge[i] = P(a, b);
		graph[a].emplace_back(P(b, i));
		graph[b].emplace_back(P(a, i));
	}
	
	for(int i = 1; i <= n; i++)
	{
		cin >> w[i];
		s += w[i];
	}

	cache.assign(n + 1, MAX_V);
	dynamic(1);

	int res = MAX_V, e = 0;
	for(int i = 1; i < n; i++)
	{
		if (res > cache[i])
		{
			res = cache[i];
			e = i;
		}
	}

	cout << res << '\n' << edge[e].first << ' ' << edge[e].second;
}