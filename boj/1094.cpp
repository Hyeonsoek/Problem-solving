#include <cstdio>
int makdea[65];
void func(int N) {
	int sum = 0,min=999,count=0;
	for(int i=1; i<65; i++) {
		if(makdea[i]>0) {
			count++;
			sum+=(i*makdea[i]);
			if(min > i) min = i;
		}
	} if(sum > N) {
		if(sum-min/2 >= N) {
			makdea[min/2]+=1;
		} else {
			makdea[min/2]+=2;
		} makdea[min]-=1;
		func(N);
	} if(sum == N) {
		printf("%d",count);
		return;
	}
}
int main() {
	int N;
	scanf("%d",&N);
	makdea[64]=1;
	func(N);
}
