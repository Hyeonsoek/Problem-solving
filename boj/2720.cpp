#include <cstdio>
int main() {
	int N;
	for (scanf("%d",&N);N--;){
		int Num,idx=0;
		scanf("%d",&Num);
		while (idx != 4) {
			idx++;
			if (idx == 1 && Num < 25) {
				printf("0 ");continue;
			} if (idx == 2 && Num < 10) {
				printf("0 ");continue;
			} if (idx == 3 && Num < 5) {
				printf("0 ");continue;
			} if (Num / 25 > 0) {
				printf("%d ",Num/25);
				Num %= 25;
				continue;
			} if (Num / 10 > 0) {
				printf("%d ",Num/10);
				Num %= 10;
				continue;
			} if (Num / 5 > 0) {
				printf("%d ",Num/5);
				Num %= 5;
				continue;
			} printf("%d\n",Num/1);
			Num %= 1;
		}
	}
}
