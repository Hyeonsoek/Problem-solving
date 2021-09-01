#include <cstdio>
#include <vector>
using namespace std;
typedef vector<int> VEC;
int n;
VEC v;

void solve(VEC &pre,int s,int cnt) {
	if(cnt==0) {
		for(int i=0; i<pre.size(); i++){
			printf("%d ",pre[i]);
		} printf("\n");
		return;
	}
	for(int i=s; i<n; i++) {
		pre.push_back(v[i]);
		solve(pre,i+1,cnt-1);
		pre.pop_back();
	}
}

int main() {
	scanf("%d",&n);
	while(n!=0) {
		VEC a;
		for(int i=0; i<n; i++) {
			int temp;
			scanf("%d",&temp);
			v.push_back(temp);
		}
		solve(a,0,6);
		v.clear();
		printf("\n");
		scanf("%d",&n);
	}
}
