#include <cstdio>
typedef long int li;
int main() {
	li M,N,map[301][301];
	li num;
	scanf("%ld%ld",&M,&N);
	for (li i = 1; i <= M; i++) {
		for (li j = 1; j <= N; j++) {
			scanf("%ld",&map[i][j]);
		}
	}
	for (scanf("%ld",&num);num--;) {
		li x,y,i,j,sum=0;
		scanf("%ld%ld%ld%ld",&x,&y,&i,&j);
		for (li k = x; k <= i; k++) {
			for (li t = y; t <= j; t++) {
				sum+=map[k][t];
			}
		}
		printf("%ld\n",sum);
	}
}
