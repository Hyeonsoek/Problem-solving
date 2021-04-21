#include <cstdio>
#define abs(a) ((a)<0?(-(a)):(a))

int main() {
	int n;
	for(scanf("%d",&n);n--;) {
		int a=0,b=0;
		char s[10];
		scanf("%s",s);
		for(int i=2,j=1; i>=0; i--,j*=26)
			b+=(s[i]-'A')*j;
		for(int i=7,j=1; i>=4; i--,j*=10)
			a+=(s[i]-'0')*j;
		if(abs(a-b)<=100)
			printf("nice\n");
		else
			printf("not nice\n");
	}
}
