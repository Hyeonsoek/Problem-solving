#include <cstdio>
#include <algorithm>
using namespace std;
int coin_num[10001];
int N,K,coin[101];

int main() {
	scanf("%d%d",&N,&K);
	for(int i=1; i<=N; i++)
		scanf("%d",&coin[i]);
	sort(coin,coin+N);
	coin_num[0] = 1;
	for(int i=1; i<=N; i++) {
		for(int j=1; j<=K; j++) {
			if(i==1 && coin[i]<=j && j%coin[i]==0)
				coin_num[j] = coin_num[j-coin[i]] + coin_num[coin[i]];
			if(i>=2 && coin[i]<=j) {
				if(coin_num[j-coin[i]]==0);
				else {
					int temp = coin_num[j-coin[i]] + coin_num[coin[i]];
					if(j%coin[i]==0) {
						int min=2100000000;
						if(coin_num[j]!=0 && coin_num[j] < min) min = coin_num[j];
						if(temp!=0 && temp < min) min = temp;
						if(j/coin[i]!=0 && j/coin[i] < min) min = j/coin[i];
						coin_num[j] = min;
					}
					else {
						if(coin_num[j]!=0&&temp!=0)
							coin_num[j] = coin_num[j] > temp ? temp : coin_num[j];
						else coin_num[j] = temp;
					}
				}
			}
		}
	}
	printf("%d",!coin_num[K] ? -1 : coin_num[K]);
}
