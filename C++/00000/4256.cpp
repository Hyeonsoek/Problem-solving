#include <iostream>
#include <vector>
using namespace std;

int n;
vector<int> pre;
vector<int> in;
vector< vector<int> > graph;

void dnq(int parent, int ps, int pe, int is, int ie)
{
	int root = pre[ps];
	graph[parent].emplace_back(root);

	if (ps >= pe || is >= ie)
		return;

	int isL = is, ieR = ie;
	int ieL = is, isR = ie;
	for (int i = is; i <= ie; i++)
	{
		if (in[i] == root)
		{
			ieL = i - 1;
			isR = i + 1;
		}
	}

	int psL = ps + 1;
	int peL = psL + ieL - isL;
	int psR = peL + 1;
	int peR = pe;

	if (peL <= peR)
		dnq(root, psL, peL, isL, ieL);

	if (psR <= peR)
		dnq(root, psR, peR, isR, ieR);
}

vector<bool> isVisited;

void dfs(int node)
{
	isVisited[node] = true;
	for (auto next : graph[node])
	{
		if (!isVisited[next])
			dfs(next);
	}
	cout << node << " ";
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int t; cin >> t;
	while (t--)
	{
		int n; cin >> n;

		isVisited.assign(n + 1, false);
		graph.assign(n + 1, vector<int>());
		
		for (int i = 0, v; i < n; i++)
		{
			cin >> v;
			pre.emplace_back(v);
		}

		for (int i = 0, v; i < n; i++)
		{
			cin >> v;
			in.emplace_back(v);
		}

		dnq(0, 0, n - 1, 0, n - 1);
		dfs(pre[0]);
		cout << "\n";

		pre.clear();
		in.clear();
	}
}