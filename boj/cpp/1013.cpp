#include <cstdio>
#include <cstring>
int len;
bool checker(char a[201],int idx,int state) {
	if(idx >= len)
		return false;
	if(a[idx] == '0') {
		switch (state) {
			case 0:
				return checker(a,idx+1,5);
			case 1:
				return checker(a,idx+1,2);
			case 2:
				return checker(a,idx+1,3);
			case 3:
				return checker(a,idx+1,3);
			case 4:
				return checker(a,idx+1,5);
			case 5:
				return false;
			case 6:
				return checker(a,idx+1,5);
		}
	}
	else {
		switch (state) {
			case 0:
				return checker(a,idx+1,1);
			case 1:
				return false;
			case 2:
				return false;
			case 3:
				if(idx+1<len)
					return checker(a,idx+1,4);
				else return true;
			case 4:
				if(idx+1<len)
					return checker(a,idx+1,4)||checker(a,idx+1,1);
				else return true;
			case 5:
				if(idx+1<len)
					return checker(a,idx+1,6);
				else return true;
			case 6:
				return checker(a,idx+1,1);
		}
	}
}

int main() {
	int T;
	for(scanf("%d",&T);T--;) {
		char s[201]={};
		scanf("%s",s);
		len = strlen(s);
		printf("%s\n",checker(s,0,0)?"YES":"NO");
	}
}