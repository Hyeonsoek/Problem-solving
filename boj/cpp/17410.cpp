#include <bits/stdc++.h>
using namespace std;

int n, sq=1500;
int arr[100010];
vector<int> bucket[1001];

void update(int index, int k)
{
    int group = index / sq;

    for(int i=0; i<bucket[group].size(); i++)
    {
        if (bucket[group][i] == arr[index])
        {
            bucket[group].erase(bucket[group].begin() + i);
            break;
        }
    }

    for(int i=0; i<=bucket[group].size(); i++)
    {
        if (i == bucket[group].size() || bucket[group][i] >= k)
        {
            bucket[group].insert(bucket[group].begin() + i, k);
            break;
        }
    }

    arr[index] = k;
}

int query(int left, int right, int k)
{
    int result = 0;
    int leftGroup = left / sq;
    int rightGroup = right / sq;

    if (leftGroup == rightGroup)
    {
        for(; left <= right; ++left)
            result += arr[left] > k;
        return result;
    }

    int leftEnd = leftGroup * sq + sq;
    for(; left < leftEnd; ++left)
        result += arr[left] > k;

    int rightStart = rightGroup * sq;
    for(; right >= rightStart; --right)
        result += arr[right] > k;

    for(int group=leftGroup+1; group<rightGroup; group++)
        result += bucket[group].end() - upper_bound(bucket[group].begin(), bucket[group].end(), k);

    return result;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n;
    for(int i=0; i<=n/sq; i++)
        bucket[i].resize(sq + 1);

    for(int i=1; i<=n; i++)
    {
        int k;
        cin >> k;
        update(i, k);
    }

    int qn;
    cin >> qn;
    while (qn--)
    {
        int q;
        cin >> q;

        if (q & 1)
        {
            int index, k;
            cin >> index >> k;
            update(index, k);
        }
        else
        {
            int left, right, k;
            cin >> left >> right >> k;
            cout << query(left, right, k) << '\n';
        }
    }
}