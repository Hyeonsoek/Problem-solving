#include <cstdio>
#include <algorithm>
using namespace std;
long N,K,coin[101],money[10001],count;
int main(){
	scanf("%d%d",&N,&K);	
	for (int i = 1; i <= N; i++)
		scanf("%d",&coin[i]);
		
	sort(coin,coin+N);
	money[0] = 1;
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= K; j++) {
			if (coin[i]<=j) {
				money[j] = money[j] + money[j-coin[i]];
			}
		}
	}
	printf("%d\n",money[K]);
}
