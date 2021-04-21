#include <cstdio>
int map[31];

int main() {
	int t;
	for(int i=0; i<28; i++) {
		scanf("%d",&t);
		map[t]=1;
	}
	for(int i=1; i<31; i++) {
		if(!map[i])
			printf("%d\n",i);
	}
}