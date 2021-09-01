#include <cstdio>

int main() {
	int coin[11],N,K,cnt=0;

	scanf("%d%d",&N,&K);
	for(int i=0; i<N; i++) {
		scanf("%d",&coin[i]);
	}

	while(K!=0 && N != 0) {
		if(K/coin[N-1] > 0) {
			cnt += K/coin[N-1];
			K %= coin[(N--)-1];
		} else N--;
	} printf("%d",cnt);
}
