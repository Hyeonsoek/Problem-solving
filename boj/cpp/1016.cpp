#include <cstdio>
typedef long long ll;
const int K = 1000001;
ll n,start,end,N,count=0;
int array[1000001];

int main(){
	scanf("%lld%lld",&start,&end);
	for(ll i=2; i*i<=end; i++){
		ll x = start/(i*i);

		if(start%(i*i)!=0) {x++;}

		while(x*(i*i)<=end) {
			array[x++*(i*i)-start]=1;
		}
	}
	for(int i=0; i<=end-start; i++) {
		if(array[i]==0) count++;
	}
	printf("%d",count);
}
