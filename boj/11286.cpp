#include <cstdio>
#include <queue>
using namespace std;

typedef pair<int,int> p;

struct cmp {
	bool operator()(p a,p b) {
		if(a.second == b.second)
			return a.first > b.first;
		else return a.second > b.second;
	}
};

int abs(int a) {return a<0?-a:a;}

priority_queue<p,vector<p>,cmp > pq;

int main() {
	int n;
	scanf("%d",&n);
	for(int i=0; i<n; i++) {
		int temp,abst;
		scanf("%d",&temp);
		if(temp < 0) abst = abs(temp);
		else abst = temp;
		if(temp == 0) {
			if(!pq.empty()) {
				printf("%d\n",pq.top().first);
				pq.pop();
			} else {
				printf("0\n");
			}
		} else {
			pq.push(p(temp,abst));
		}
	}
}
