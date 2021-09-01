#include <cstdio>
#include <algorithm>
using namespace std;
int main() {
	int N,F[1001];
	scanf("%d",&N);
	for (int i = 0; i < N; i++){
		scanf("%d",&F[i]);
	} sort(F,F+N);
	for (int i = 0; i < N; i++) {
		printf("%d\n",F[i]);
	}
}
