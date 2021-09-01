#include <cstdio>
#include <cmath>
#include <vector>
typedef long long Long;
using namespace std;

Long init(vector<Long> &a,vector<Long> &tree,
		int node,int start,int end)
{
	if(start == end)
		return tree[node] = a[end];
	else
	{
		int left = init(a,tree,node*2,start,(start+end)/2);
		int right = init(a,tree,node*2+1,(start+end)/2+1,end);
		return tree[node] = left > right ? right : left;
	}
}

Long min(vector<Long> &tree,int node,int start,int end,
		int left,int right)
{
	if(end < left || right < start)
		return 1000000001;
	if(left <= start && end <= right)
		return tree[node];
	int LL = min(tree,node*2,start,(start+end)/2,left,right);
	int RR = min(tree,node*2+1,(start+end)/2+1,end,left,right);
	return LL > RR ? RR : LL;
}

int main()
{
	int n,m;
	scanf("%d%d",&n,&m);
	vector<Long> v(n);
	for(int i=0; i<n; ++i)
		scanf("%lld",&v[i]);
	int H = (int)ceil(log2(n));
	int tree_size = (1<<(H+1));
	vector<Long> tree(tree_size);
	init(v,tree,1,0,n-1);
	for(int i=0; i<m; ++i)
	{
		int start,end;
		scanf("%d%d",&start,&end);
		printf("%lld\n",min(tree,1,0,n-1,start-1,end-1));
	}
}