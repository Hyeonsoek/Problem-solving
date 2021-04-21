#include <cstdio>
int c;

int main() {
	int k,t=-1000001;
	for(;scanf("%d",&k)!=EOF;) {
		if(k >= t)
			t = k;
		else { printf("Bad"); return 0; }
	}
	printf("Good");
}