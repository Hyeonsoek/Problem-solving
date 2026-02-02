#include <iostream>
#include <string>
#include <map>
constexpr auto ROOT = "";
using namespace std;

struct Node
{
	string value;
	map<string, Node*> children;

	Node(string val) : value(val) {}

	Node* tryInsert(string value)
	{
		if (hasChild(value))
			return children[value];

		return children[value] = new Node(value);
	}

	bool hasChild(string value)
	{
		return children.find(value) != children.end();
	}

	bool operator <(const Node& other) const
	{
		return value < other.value;
	}
};

void dfs(Node* node, int h)
{
	for (auto& [next, node] : node->children)
	{
		for (int i = 0; i < h; i++)
			cout << "--";
		cout << node->value << '\n';
		dfs(node, h + 1);
	}
}

int main()
{
	int n;
	Node* root = new Node("");

	cin >> n;

	for(int i = 0; i < n; i++)
	{
		int k; cin >> k;
		Node* parent = root;

		for (int j = 0; j < k; j++)
		{
			string str; cin >> str;
			parent = parent->tryInsert(str);
		}
	}

	dfs(root, 0);
}