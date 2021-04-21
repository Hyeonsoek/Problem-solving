#include <cstdio>
#include <cstring>

int main() {
	char a[1001]={};
	int n;
	scanf("%s%d",a,&n);
	int len = strlen(a);
	int cnt=0;
	for(int i=len-1,j=1; i>=0; i--,j*=n) {
		if(a[i]>='A' && a[i]<='Z')
			cnt += (a[i]-'A'+10)*j;
		else cnt += (a[i]-'0')*j;
	}
	printf("%d\n",cnt);
}