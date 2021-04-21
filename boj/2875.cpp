#include <cstdio>
int main() {
	int N,M,K;
	scanf("%d%d%d",&N,&M,&K);
	while(K!=0) {
		if(N/2 == M) {
			if(K>=3) {
				N-=2,M-=1;
				K-=3;
			} else {
				N-=K;
				K-=K;
			} continue;
		}
		
		if(N/2 > M) {
			if(K>=2) {
				N-=2;
				K-=2;
			} else {
				N-=K;
				K-=K;
			}
		}
		
		if(N/2 < M) {
			M-=1;
			K-=1;
		}
	} 
	printf("%d",N/2>M?M:N/2);
}
