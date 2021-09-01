#include <cstdio>
#include <utility>
#define min(a,b) ((a>b)?b:a)
using namespace std;
typedef long long llong;

int box[1000001];
int n,k,d;
pair< pair<int,int>, int> rules[10001];

llong bsearch(int low,int high)
{
	if(low == high)
		return low;
	if(high < low)
		return -1;
	int mid = (low + high) / 2;
	llong sum = 0;

	for(int i=0; i<k; ++i)
	{
		pair<int,int> &pos = rules[i].first;
		int &indent = rules[i].second;
		int nhigh = min(pos.second,mid);

		if(pos.first <= nhigh)
			sum += (nhigh - pos.first) / indent + 1; 
	}

	if(sum >= d)
		return bsearch(low,mid);
	else
		return bsearch(mid+1,high);
}

int main()
{
	scanf("%d%d%d",&n,&k,&d);
	for(int i=0; i<k; ++i)
	{
		pair<int,int> &pos = rules[i].first;
		scanf("%d%d%d",&pos.first,&pos.second,&rules[i].second);
	}

	printf("%lld\n",bsearch(0,n));
}