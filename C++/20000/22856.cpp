#include <iostream>
#include <vector>
using namespace std;

struct Node
{
	int r, l, v;
	Node(int v, int l, int r) : v(v), l(l), r(r) {};
};

int n;
Node* nodes[100'001];

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> n;

	for (int i = 0, a, b, c; i < n; i++)
	{
		cin >> a >> b >> c;
		nodes[a] = new Node(a, b, c);
	}

	int b, res = 0;
	for (b = 1; b != -1; b = nodes[b]->r, res++);

	cout << 2 * (n - 1) - res + 1;
}