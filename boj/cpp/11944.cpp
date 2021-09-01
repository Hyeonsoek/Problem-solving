#include <cstdio>
#include <cstring>
#include <cstdlib>
int main() {
	char a[5];
    int M;
    scanf("%s%d",a,&M);
	int len=strlen(a),b=atoi(a);
	if(len*b > M) {
   		for(int i=0; i<M; i++)
    		printf("%c",a[i%len]);
	}
	else {
		for(int i=0; i<b; i++)
			printf("%s",a);
	}
}
