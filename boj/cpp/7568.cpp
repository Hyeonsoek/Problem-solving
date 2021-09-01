#include <cstdio>
#include <vector>
#include <utility>
using namespace std;
vector<pair<int,int> > v;
vector<int> Rank(51);
int N;

int main()
{
	scanf("%d",&N);
	for(int i=0; i<N; ++i)
	{
		int a,b;
		scanf("%d%d",&a,&b);
		v.push_back(make_pair(a,b));
	}

	for(int i=0; i<N; ++i)
	{
		for(int j=0; j<N; ++j)
		{

			if(i == j)
				continue;

			if(v[i].first > v[j].first && v[i].second > v[j].second)
				++Rank[j];
		}
	}

	for(int i=0; i<N; ++i)
		printf("%d ",Rank[i]+1);
}