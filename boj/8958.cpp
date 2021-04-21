#include <cstdio>
#include <cstring>
int main() {
	int N;
	for (scanf("%d",&N);N--;){
		char input[101];
		scanf("%s",input);
		int size = strlen(input),sum=0,count=1;
		for (int i = 0; i < size; i++) {
			if (input[i]=='O') {
				sum+=count;
				count++;
			} if (input[i]=='X') {
				count=1;
			}
		} printf("%d\n",sum);
	}
}
