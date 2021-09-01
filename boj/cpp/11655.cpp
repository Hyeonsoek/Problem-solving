#include <cstdio>
#include <cstring>

char c[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
char m[] = "abcdefghijklmnopqrstuvwxyz";

int main() {
	char a[101];
	gets(a);
	for(int i=0;i<strlen(a);i++) {
		if(a[i] >= 'A' && a[i] <= 'Z') {
			printf("%c",c[a[i]+13>'Z'?a[i]-13-'A':a[i]+13-'A']);
			continue;
		}
		if(a[i] >= 'a' && a[i] <= 'z') {
			printf("%c",m[a[i]+13>'z'?a[i]-13-'a':a[i]+13-'a']);
			continue;
		}
		printf("%c",a[i]);
	}
}
