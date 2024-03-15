/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>
#include <vector>
#define MAX 100001
using namespace::std;

int n;
vector<int> tree(MAX * 4);
vector<int> arr(MAX);

void init(int node, int start, int end)
{
    if (start == end)
    {
        tree[node] = 1;
        return;
    }

    int mid = (start + end) / 2;
    init(node * 2, start, mid);
    init(node * 2 + 1, mid + 1, end);

    tree[node] = tree[node * 2] + tree[node * 2 + 1];
}

void update(int node, int start, int end, int index, int value)
{
    if (index < start or end < index)
        return;

    if (start == end)
    {
        tree[node] += value;
        return;
    }

    int mid = (start + end) / 2;
    update(node * 2, start, mid, index, value);
    update(node * 2 + 1, mid + 1, end, index, value);

    tree[node] = tree[node * 2] + tree[node * 2 + 1];
}

int query(int node, int start, int end, int k)
{
    if (start == end)
        return start;

    int mid = (start + end) / 2;
    int LL = tree[node << 1];

    if (k <= LL)
        return query(node * 2, start, mid,  k);
    return query(node * 2 + 1, mid + 1, end, k - LL);
}

int main()
{
    cin >> n;
    for(int i=0; i<n; i++)
        cin >> arr[i];

    init(1, 1, n);

    vector<int> result(n);
    for(int i=0; i<n; i++)
    {
        int index = query(1, 1, n, arr[i]+1);
        result[index - 1] = i + 1;
        update(1, 1, n, index, -1);
    }

    for(int i=0; i<n; i++)
        cout << result[i] << '\n';

    return 0;
}