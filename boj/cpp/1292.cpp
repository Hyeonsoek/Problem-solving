#include <cstdio>
int input[1001];
int main() {
	int start,end,count=1,sum=0;
	scanf("%d%d",&start,&end);
	for (int i=1; i<47; i++) {
		for (int j=0; j<i; j++) {
			if (count<=1000) {
				input[count++] = i;
			}
		}
	}
	for (int i=start; i<=end; i++) {
		sum += input[i];
	} printf("%d",sum);
}
