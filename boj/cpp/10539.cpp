#include <cstdio>

int main() {
	int N;
	int B[102]={};
	scanf("%d",&N);
	for(int i=1; i<=N; i++)
		scanf("%d",&B[i]);
	int A[102]={};
	A[1] = B[1];
	printf("%d ",A[1]);
	
	if(N == 1) return 0;
	
	for(int i=2; i<=N; i++) {
		int temp = B[i]*i;
		for(int j=0; j<i; j++) {
			temp -= A[j];
		}
		printf("%d ",temp);
		A[i] = temp;
	}
}
