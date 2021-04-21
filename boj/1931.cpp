#include <cstdio>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

int main()
{
	int N;
	vector< pair<int,int> > v;
	scanf("%d",&N);
	for(int i=0; i<N; ++i)
	{
		int x,y;
		scanf("%d%d",&x,&y);
		v.push_back(make_pair(y,x));
	}

	sort(v.begin(),v.end());
	int cur = v[0].first;
	int cnt = 1;
	for(int i=1; i<N; ++i)
	{
		if(cur <= v[i].second)
		{
			cur = v[i].first;
			cnt++;
		}
	}
	printf("%d\n",cnt);
}