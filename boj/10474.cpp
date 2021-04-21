#include <cstdio>
int main() {
	long long N,M;
	scanf("%lld%lld",&N,&M);
	while (N!=0||M!=0) {
		if (M!=0) {
			printf("%lld %lld / %lld\n",N/M,N%M,M);
		} scanf("%lld%lld",&N,&M);
	}
}
