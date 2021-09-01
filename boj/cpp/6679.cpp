#include <cstdio>

int solve(int i,int s) {
	int count=0;
	while(i!=0) {
		count += (i%s);
		i/=s;
	}
	return count;
}

int main() {
	for(int i=1000; i<10000; i++) {
		int hex = solve(i,16);
		int duo = solve(i,12);
		int dem = solve(i,10);
		if(hex == duo && duo == dem)
			printf("%d\n",i);
	}
}