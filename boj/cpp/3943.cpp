#include <cstdio>
int main() {
	int T;
	for(scanf("%d",&T);T--;) {
		int a;
		scanf("%d",&a);
		int max = a;
		while(a!=1) {
			if(a%2==0)
				a/=2;
			else {
				a*=3;
				a++;
			}
			if(max < a)
				max = a;
		}
		printf("%d\n",max);
	}
}
