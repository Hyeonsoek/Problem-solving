#include <cstdio>
#include <cstring>

int main() {
	char a[101];
	while(gets(a)) {
		int blank=0,capytal=0,small=0,num=0;
		for(int i=0; i<strlen(a); i++) {
			if(a[i]==' ')
				blank++;
			if(a[i]>='a' && a[i]<='z')
				small++;
			if(a[i]>='A' && a[i]<='Z')
				capytal++;
			if(a[i]>='0' && a[i]<='9')
				num++;
		}
		printf("%d %d %d %d\n",small,capytal,num,blank);
	}
}
