#include <iostream>
#include <string>
#include <vector>
#include <set>
using namespace std;

struct Node
{
	int value;
	Node* l = NULL;
	Node* r = NULL;

	Node(int val) : value(val) {}
};

struct Tree
{
	Node* root;

	Tree(int r) : root(new Node(r)) {}

	void insert(int value)
	{
		Node* v = new Node(value);
		Node* r = root;

		while (r != NULL)
		{
			if (r->value < v->value)
			{
				if (r->r == NULL)
				{
					r->r = v;
					break;
				}
				
				r = r->r;
			}
			else
			{
				if (r->l == NULL)
				{
					r->l = v;
					break;
				}

				r = r->l;
			}
		}
	}

	string preorder()
	{
		return preorder(root);
	}

	string inorder()
	{
		return inorder(root);
	}

private:
	string preorder(Node* node)
	{
		string ret = "M";

		if (node->l != NULL)
			ret += "L" + preorder(node->l);

		if (node->r != NULL)
			ret += "R" + preorder(node->r);

		return ret;
	}

	string inorder(Node* node)
	{
		string ret = "";

		if (node->l != NULL)
			ret += "L" + inorder(node->l);

		ret += "M";

		if (node->r != NULL)
			ret += "R" + inorder(node->r);

		return ret;
	}
};

int n, k;

int main()
{
	cin >> n >> k;

	set<string> pr;
	set<string> in;

	for (int i = 0; i < n; i++)
	{
		int v; cin >> v;
		Tree tree = Tree(v);

		for (int j = 1; j < k; j++)
		{
			cin >> v;
			tree.insert(v);
		}

		pr.insert(tree.preorder());
		in.insert(tree.inorder());
	}

	cout << max(pr.size(), in.size()) << '\n';
}