#include <cstdio>
int T,tri[160],check;

void solve(int num,int value,int k,int cnt) {
	if(check) return;
	if(cnt == 0) {
		if(num == value) check=1;
		return;
	}
	for(int i=1; i<=k; i++) {
		solve(num,tri[i]+value,k,cnt-1);
	}
}
int main() {
	scanf("%d",&T);
	for(int i=1; i<160; i++) {
		tri[i] = ((i+1)*i)/2;
	}
	for(int i=0; i<T; i++) {
		int num,k=0;
		scanf("%d",&num);
		while(num > tri[k++]);
		solve(num,0,k-1,3);
		printf("%d\n",check);
		check=0;
	}
}