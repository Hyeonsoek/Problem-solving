#include <cstdio>
int main() {
	int N,count=0,che[1001]={1,1};
	for (int i=2; i < 1001; i++){
		if (!che[i]) {
			for (int j = 2*i; j < 1001; j+=i) {
				che[j] = 1;
			}
		}
	}
	for (scanf("%d",&N);N--;) {
		int prim;
		scanf("%d",&prim);
		if (!che[prim]) count++;
	} printf("%d",count);
}
