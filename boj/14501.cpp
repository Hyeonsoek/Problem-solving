#include <utility>
#include <vector>
#include <cstdio>
using namespace std;
typedef pair<int,int> dm;
vector<dm> v;
int n,maxi =-1;

void brute(vector<dm> &vv,int days)
{
	if(days == n)
	{
		int sum = 0;
		for(int i=0; i<vv.size(); ++i)
			sum += vv[i].second;
		if(sum > maxi)
			maxi = sum;
	}
	else
	{	
		if(days + v[days].first <= n)
		{
			vv.push_back(v[days]);
			brute(vv,days+v[days].first);
			vv.pop_back();
		}

		if(days + 1 <= n)
			brute(vv,days+1);
	}
}

int main()
{
	scanf("%d",&n);
	for(int i=0; i<n; ++i)
	{
		int a,b;
		scanf("%d%d",&a,&b);
		v.push_back(dm(a,b));
	}
	vector<dm> temp;
	brute(temp,0);
	printf("%d\n",maxi);
}