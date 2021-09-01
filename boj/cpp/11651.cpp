#include <cstdio>
#include <algorithm>
#include <vector>
#include <utility>
using namespace std;
vector< pair<int,int> > v;

bool sec(const pair<int,int> &a,
		const pair<int,int> &b)
{
	if(a.second < b.second)
		return true;
	else if(a.second == b.second)
		return a.first < b.first;
	else
		return false;
}

int main()
{
	int n;
	scanf("%d",&n);
	for(int i=0; i<n; ++i)
	{
		int a,b;
		scanf("%d%d",&a,&b);
		v.push_back(make_pair(a,b));
	}
	sort(v.begin(),v.end(),sec);
	for(int i=0; i<n; ++i)
		printf("%d %d\n",v[i].first,v[i].second);
}