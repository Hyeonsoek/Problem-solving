#include <bits/stdc++.h>
using namespace std;

int n;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n;
    for (int p, i = 1; i < n; i++)
        cin >> p;

    vector<int> v;
    for (int a, i = 0; i < n; i++)
    {
        cin >> a;
        v.emplace_back(a);
    }

    sort(v.begin(), v.end(), greater<int>());

    size_t j = 0;
    for (int i = 0; i < n; i++)
    {
        j += v[i];
        cout << j << '\n';
    }

    return 0;
}