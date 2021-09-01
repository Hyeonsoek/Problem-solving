#include <cstdio>
int main() {
	int N,max=-1;
	scanf("%d",&N);
	for (int i = 0; i < N; i++) {
		int a,b,c,money;
		scanf("%d%d%d",&a,&b,&c);
		if (a == b && b == c) {
			money = 10000 + a*1000;
		} else if (a == b || b == c || a == c) {
			if (a == b) money = 1000+a*100;
			if (b == c) money = 1000+b*100;
			if (a == c) money = 1000+c*100;
		} else {
			if ((a > b && b > c) || (a > c && c > b)) money = a*100;
			if ((b > a && a > c) || (b > c && c > a)) money = b*100;
			if ((c > a && a > b) || (c > b && b > a)) money = c*100;
		}
		if (max < money) max = money;
	}
	printf("%d",max);
}
