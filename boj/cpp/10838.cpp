#include <bits/stdc++.h>
using namespace std;

struct node
{
    int parent=0, color=0;
};

int n, k;
int visited[100001];
vector<node> tree;

int LCA(int u, int v, int k)
{
    for (int count=0; count < 1000; count++)
    {
        visited[u] = k;
        u=tree[u].parent;
    }

    for (int count=0; count < 1000; count++)
    {
        if (visited[v] == k)
            return v;

        v = tree[v].parent;
    }

    return 0;
}

void paint(int u, int v, int color, int k)
{
    int lca = LCA(u, v, k);
    while (u != lca)
    {
        tree[u].color = color;
        u = tree[u].parent;
    }

    while (v != lca)
    {
        tree[v].color = color;
        v = tree[v].parent;
    }
}

int count(int u, int v, int k)
{
    set<int> result;
    int lca = LCA(u, v, k);
    while (u != lca)
    {
        result.insert(tree[u].color);
        u = tree[u].parent;
    }

    while (v != lca)
    {
        result.insert(tree[v].color);
        v = tree[v].parent;
    }

    return result.size();
}

void move(int u, int v)
{
    tree[u].parent = v;
}

int main()
{
    cin.tie(NULL);cout.tie(NULL);
    ios_base::sync_with_stdio(false);

    cin >> n >> k;
    tree.reserve(n);

    for (int i=1; i<=k; i++)
    {
        int r;
        cin >> r;

        if (r == 1)
        {
            int a, b, c;
            cin >> a >> b >> c;
            paint(a, b, c, i);
        }
        else if (r == 2)
        {
            int a, b;
            cin >> a >> b;
            move(a, b);
        }
        else if (r == 3)
        {
            int a, b;
            cin >> a >> b;
            cout << count(a, b, i) << '\n';
        }
    }

    return 0;
}