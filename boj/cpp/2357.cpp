#include <cstdio>
#include <cmath>
#include <vector>
typedef long long Long;
using namespace std;

Long init_max(vector<Long> &a,vector<Long> &tree,
		int node,int start,int end)
{
	if(start == end)
		return tree[node] = a[end];
	else
	{
		int left = init_max(a,tree,node*2,start,(start+end)/2);
		int right = init_max(a,tree,node*2+1,(start+end)/2+1,end);
		return tree[node] = left < right ? right : left;
	}
}

Long init_min(vector<Long> &a,vector<Long> &tree,
		int node,int start,int end)
{
	if(start == end)
		return tree[node] = a[end];
	else
	{
		int left = init_min(a,tree,node*2,start,(start+end)/2);
		int right = init_min(a,tree,node*2+1,(start+end)/2+1,end);
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

Long max(vector<Long> &tree,int node,int start,int end,
		int left,int right)
{
	if(end < left || right < start)
		return 0;
	if(left <= start && end <= right)
		return tree[node];
	int LL = max(tree,node*2,start,(start+send)/2,left,right);
	int RR = max(tree,node*2+1,(start+end)/2+1,end,left,right);
	return LL > RR ? LL : RR;
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
	vector<Long> max_tree(tree_size);
	vector<Long> min_tree(tree_size);
	init_min(v,min_tree,1,0,n-1);
	init_max(v,max_tree,1,0,n-1);
	for(int i=0; i<m; ++i)
	{
		int start,end;
		scanf("%d%d",&start,&end);
		printf("%lld ",min(min_tree,1,0,n-1,start-1,end-1));
		printf("%lld\n",max(max_tree,1,0,n-1,start-1,end-1));
	}
}