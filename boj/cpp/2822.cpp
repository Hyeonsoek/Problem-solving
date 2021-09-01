#include <cstdio>
#include <algorithm>
using namespace std;
int main() {
	int T[9] = {},idx[9]={},Sum=0;
	for (int i = 0; i < 8; i++) {
		scanf("%d",&T[i]);
		idx[i] = i+1;
	} for (int i = 0; i < 8; i++) {
		for (int j = 0; j < 7; j++) {
			if (T[j] > T[j+1]) {
				int temp = T[j];
				T[j] = T[j+1];
				T[j+1] = temp;
				temp = idx[j];
				idx[j] = idx[j+1];
				idx[j+1] = temp;
			}
		}
		Sum += T[8-i-1];
	} Sum -= T[0] + T[1] + T[2];
	printf("%d\n",Sum);
	for (int i = 3; i < 8; i++) {
		for (int j = 3; j < 7; j++) {
			if (idx[j] > idx[j+1]) {
				int temp = idx[j];
				idx[j] = idx[j+1];
				idx[j+1] = temp;
			}
		}
	} for (int i = 3; i < 8; i++) {
		printf("%d ",idx[i]);
	}
}
