#include <cstdio>
int stack[10001],top;
int main()
{
	int N;
	for (scanf("%d",&N);N--;){
		int num;
		char input[101] = {};
		scanf("%s",input);
		if (input[1] == 'u') {
			scanf("%d",&num);
			stack[top++] = num;
			continue;
		} if (input[0] == 't') {
			if (top > 0) printf("%d\n",stack[top-1]);
			else printf("-1\n");
		} if (input[0] == 'p') {
			if (top>0) {
				printf("%d\n",stack[top-1]);
				stack[--top] = 0;
			} else printf("-1\n");
		} if (input[0] == 's') {
			printf("%d\n",top);
		} if (input[0] == 'e') {
			printf("%s\n",top>0?"0":"1");
		}
	}
}
