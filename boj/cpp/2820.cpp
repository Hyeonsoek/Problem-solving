#include <bits/stdc++.h>
#include <iostream>
using namespace std;

typedef pair<int, int> Query;

int n, m;
vector<Query> queries;
vector<int> graph[500001];
vector<long> arr;
vector<long> tree;
vector<long> lazy;

void propagate(int node, int start, int end)
{
    if (lazy[node])
    {
        if (start != end)
        {
            lazy[node << 1] += lazy[node];
            lazy[node << 1 | 1] += lazy[node];
        }
        
        tree[node] += (end - start + 1) * lazy[node];
        lazy[node] = 0;
    }
}

void update(int left, int right, long value, int node=1, int start=1, int end=n)
{
    propagate(node, start, end);
    
    if (end < left || right < start)
        return;
    
    if (left <= start && end <= right)
    {
        lazy[node] += value;
        propagate(node, start, end);
        return;
    }
    
    int mid = (start + end) >> 1;
    update(left, right, value, node << 1, start, mid);
    update(left, right, value, node << 1 | 1, mid + 1, end);
    
    tree[node] = tree[node << 1] + tree[node << 1 | 1];
}

long query(int index, int node=1, int start=1, int end=n)
{
    propagate(node, start, end);
    
    if (start == end)
        return tree[node];
        
    int mid = (start + end) >> 1;
    if (index > mid)
        return query(index, node << 1 | 1, mid + 1, end);
    else
        return query(index, node << 1, start, mid);
}

int euler(int node, int start)
{
    queries[node].first = start;
    for(auto x : graph[node])
    {
        if (!queries[x].first)
            start = euler(x, start + 1);
    }
    queries[node].second = start;
    return start;
}

int main()
{
    cin.tie(0); cout.tie(0);
    ios_base::sync_with_stdio(false);
    
    cin >> n >> m;
    arr.resize(n + 1, 0);
    queries.resize(n + 1, {0, 0});
    tree.reserve(4 * n);
    lazy.reserve(4 * n);
    
    cin >> arr[1];
    for(int i=2; i<=n; i++)
    {
        int parent;
        cin >> arr[i] >> parent;
        graph[parent].push_back(i);
    }
    
    euler(1, 1);
    
    for(int i=1; i<=n; i++)
    {
        int index = queries[i].first;
        update(index, index, arr[i]);
    }
    
    while(m--)
    {
        char q; cin >> q;
        
        if (q == 'p')
        {
            int index;
            long value;
            cin >> index >> value;
            
            int left = queries[index].first + 1;
            int right = queries[index].second;
            
            if (left > right)
                continue;
            
            update(left, right, value);
        }
        else
        {
            int index; cin >> index;
            cout << query(queries[index].first) << '\n';
        }
    }

    return 0;
}