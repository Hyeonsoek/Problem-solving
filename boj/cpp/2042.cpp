#include <cstdio>
#include <cmath>
#include <vector>
using namespace std;

long long init(vector<long long> &a, vector<long long> &tree,
	int node, int start, int end) {
	if(start == end)
		return tree[node] = a[start];
	else
		return tree[node] = init(a,tree,node*2,start,(start+end)/2) +
			init(a,tree,node*2+1,(start+end)/2+1,end);
}

long long sum(vector<long long> &tree, int node,int start,int end,
		int left,int right)
{
	if(left > end || right < start)
		return 0;
	if(left <= start && end <= right)
		return tree[node];
	return sum(tree,node*2,start,(start+end)/2,left,right) +
		sum(tree,node*2+1,(start+end)/2+1,end,left,right);
}

void update(vector<long long> &tree, int node, int start, int end,
		int index,long long diff)
{
	if (index < start || index > end)
		return;
	tree[node] += diff;
	if(start != end)
	{
		update(tree,node*2,start,(start+end)/2,index,diff);
		update(tree,node*2+1,(start+end)/2+1,end,index,diff);
	}
}

int main() {
	int n,m,k;
	scanf("%d%d%d",&n,&m,&k);
	vector<long long> v(n);
	for(int i=0; i<n; ++i)
		scanf("%lld",&v[i]);
	int h = (int)ceil(log2(n));
	int tree_size = (1<<(h+1));
	vector<long long> tree(tree_size);
	init(v,tree,1,0,n-1);
	for(int i=0; i<m+k; ++i)
	{
		long long a,b,c;
		scanf("%lld%lld%lld",&a,&b,&c);
		if(a == 1)
		{
			update(tree,1,0,n-1,b-1,c-v[b-1]);
			v[b-1] = c;
		}
		if(a == 2)
		{
			long long k = sum(tree,1,0,n-1,b-1,c-1);
			printf("%lld\n",k);
		}
	}
}