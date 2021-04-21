#include <cstdio>
#include <algorithm>
using namespace std;
int main() {
	int F[4];
	for (int i = 0; i < 3; i++){
		scanf("%d",&F[i]);
	} sort(F,F+3);
	for (int i = 0; i < 3; i++) {
		printf("%d ",F[i]);
	}
}
