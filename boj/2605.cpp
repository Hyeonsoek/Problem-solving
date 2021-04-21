#include <cstdio>
int main() {
	int N,Input[101],array[101];
	scanf("%d",&N);
	for (int i = 0; i < N; i++) {
		scanf("%d",&Input[i]);
		array[i] = i+1;
	} for (int i = 0; i < N; i++) {
		for (int j = i; j > i-Input[i] ; j--) {
			if (j-1 >=0) {
				int temp = array[j-1];
				array[j-1] = array[j];
				array[j] = temp;
			}
		}
	} for (int i = 0 ; i < N; i++)
		printf("%d ",array[i]);
}
