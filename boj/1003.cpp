#include <cstdio>
int N,temp;
int zero[42] = {1,0,1};
int one[41] = {0,1};

int main() {
	scanf("%d",&N);
	for(int i=1; i<40; i++) {
		zero[i+2] = zero[i+1] + zero[i];
		one[i+1] = one[i] + one[i-1];
	}
	for(int i=0; i<N; i++) {
		scanf("%d",&temp);
		printf("%d %d\n",zero[temp],one[temp]);
	}
}