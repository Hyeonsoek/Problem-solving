#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <queue>
using namespace std;
typedef pair<double,int> p;
priority_queue<p,vector<p>,greater<p> > pq;

bool cmp(p &a,p &b) {
	if(a.first == b.first)
		return a.second < b.second;
	return a.first < b.first;
}

int main() {
	int T;
	scanf("%d",&T);
	for(int i=0; i<T; i++) {
		double a,b,c;
		scanf("%lf%lf%lf",&a,&b,&c);
		pq.push(p((sqrt(a*a+b*b))/c,i+1));
	}
	while(!pq.empty()) {
		p t = pq.top();
		printf("%d\n",t.second);
		pq.pop();
	}
}
