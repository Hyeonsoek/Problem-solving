#include <cstdio>
#include <vector>
using namespace std;
typedef vector<int> VEC;
int oneto[3] = {1,2,3},count;

void solve(int temp,VEC &pre) {
	int sum = 0;
	for(int i=0; i<pre.size(); i++)
		sum += pre[i];
	if(sum == temp) { count++; return; }
	for(int i=0; i<3; i++) {
		int sum = 0;
		pre.push_back(oneto[i]);
		for(int i=0; i<pre.size(); i++)
			sum+=pre[i];
		if(sum <= temp) solve(temp,pre);
		pre.pop_back();
	}
}

int main() {
	int T,temp;
	scanf("%d",&T);
	for(int i=0; i<T; i++) {
		VEC v;
		scanf("%d",&temp);
		solve(temp,v);
		printf("%d\n",count);
		count=0;
	}
}
