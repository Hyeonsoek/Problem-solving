#include <cstdio>
int queue[10001],front,rear,N;
int main() {
	scanf("%d",&N);
	for (int i = 0; i<N; i++) {
		char input[10]={};
		scanf("%s",input);
		int K;
		if (input[3]=='h') {
			scanf("%d",&K);
			queue[rear++] = K;
			continue;
		} if (input[1]=='o') {
			if (rear-front<=0) {
				printf("-1\n");
				continue;
			} printf("%d\n",queue[front]);
			queue[front++] = 0;
			continue;
		} if (input[0]=='s') {
			printf("%d\n",rear-front);
			continue;
		} if (input[0]=='f') {
			if (rear-front<=0)
				printf("-1\n");
			else printf("%d\n",queue[front]);
			continue;
		} if (input[3]=='k') {
			if (rear-front<=0)
				printf("-1\n");
			else printf("%d\n",queue[rear-1]);
			continue;
		} if (input[0]=='e') {
			if (rear-front<=0)
				printf("1\n");
			else printf("0\n");
			continue;
		}
	}
}
