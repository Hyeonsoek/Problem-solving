#include <cstdio>
#include <queue>
using namespace std;

priority_queue<int> pq;

int main() {
	int n;
	scanf("%d",&n);
	for(int i=0; i<n; i++) {
		int temp;
		scanf("%d",&temp);
		if(temp == 0) {
			if(!pq.empty()) {
				printf("%d\n",pq.top());
				pq.pop();
			} else {
				printf("0\n");
			}
		} else {
			pq.push(temp);
		}
	}
}