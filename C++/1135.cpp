#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n, d;
vector< vector<int> > graph;

int dfs(int vertex)
{
	if (graph[vertex].size() == 0)
		return 0;

	vector<int> r;
	for (auto n : graph[vertex])
	{
		r.emplace_back(dfs(n));
	}

	sort(r.begin(), r.end(), greater<int>());

	int v = 0;
	for (int i = 0; i < r.size(); i++)
		v = max(v, r[i] + i + 1);
	return v;
}

int main()
{
	cin >> n;
	graph.assign(n, vector<int>());

	cin >> d;
	for (int c = 1, p; c < n; c++)
	{
		cin >> p; 
		graph[p].emplace_back(c);
	}

	cout << dfs(0);
}