#include <iostream>
#include <vector>
#include <bits/stdc++.h>
#define MAX 300001
#define MOD 998244353
using namespace std;
typedef long long lld;
typedef tuple<int, int, int> Query;

struct node
{
    lld value = 0, weight = 0, lazy = -1;
};

lld n, q;
vector<Query> queries;
vector<node> tree;

void build(int node, int start, int end)
{
    if (start == end)
    {
        tree[node].weight = 1LL * start * (n - start + 1);
        tree[node].weight %= MOD;
        return;
    }

    int mid = (start + end) >> 1;
    build(node << 1, start, mid);
    build(node << 1 | 1, mid + 1, end);

    tree[node].weight = tree[node << 1].weight + tree[node << 1 | 1].weight;
    tree[node].weight %= MOD;
}

void propagate(int node, int start, int end)
{
    if (tree[node].lazy >= 0)
    {
        if (start != end)
        {
            tree[node << 1].lazy = tree[node].lazy;
            tree[node << 1 | 1].lazy = tree[node].lazy;
        }

        tree[node].value = tree[node].lazy * tree[node].weight % MOD;
        tree[node].lazy = -1;
    }
}

void update(int node, int start, int end, int left, int right, lld value)
{
    propagate(node, start, end);

    if (right < start || end < left)
        return;

    if (left <= start && end <= right)
    {
        tree[node].lazy = value;
        propagate(node, start, end);
        return;
    }

    int mid = (start + end) / 2;
    update(node << 1, start, mid, left, right, value);
    update(node << 1 | 1, mid + 1, end, left, right, value);

    tree[node].value = tree[node << 1].value + tree[node << 1 | 1].value;
    tree[node].value %= MOD;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    cin >> n >> q;

    tree.reserve(4*n);
    build(1, 1, n);

    lld result = 0;
    for (int i = 1; i <= q; i++)
    {
        int left, right; lld c;
        cin >> left >> right >> c;
        c = c * i % MOD;

        update(1, 1, n, left, right, c);
        result = (result + tree[1].value) % MOD;
    }

    cout << result;

    return 0;
}