#include <cstdio>
int a[27];
int main() {
	char input[101];
	scanf("%s",input);
	for (int i=0;input[i]!='\0';i++){
		if (a[input[i]-'a']==0)
			a[input[i]-'a']=i+1;
	} for (int i=0;i<26;i++){
		printf("%d ",a[i]-1);
	}
}
