#include <cstdio>
#include <algorithm>
using namespace std;
int main() {
	int count=-1,N,num[10001];
	scanf("%d",&N);
	for (int i = 0; i < N; i++) {
		scanf("%d",&num[i]);
	} sort(num,num+N);
	if (N%2==0) {
		printf("%d",num[N/2-1]*num[N/2]);
	} if (N%2==1) {
		printf("%d",num[N/2]*num[N/2]);
	}
}
