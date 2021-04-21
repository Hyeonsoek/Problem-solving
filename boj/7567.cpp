#include <cstdio>
#include <cstring>
int main() {
	char input[51]={};
	scanf("%s",input);
	int count=10,len = strlen(input);
	for (int i=1; i<len; i++) {
		if (input[i] == input[i-1])
			count+=5;
		if (input[i] != input[i-1])
			count+=10;
	}
	printf("%d",count);
}
