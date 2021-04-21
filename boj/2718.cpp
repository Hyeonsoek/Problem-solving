#include <cstdio>
#include <cstring>
int T,k,value[1001];
int search(int num) {
	if(num < 2) return 1;
	if(num == 2) return 5;
	int &ret = value[num];
	if(ret != -1) return ret;
	ret = search(num-1) + search(num-2)*4;
	for(int i=3; i<=num; i++) 
		ret += search(num-i)*(2+i%2^1);
	return ret;
}

int main() {
	scanf("%d",&T);
	memset(value,-1,sizeof(value));
	for(int i=0;i<T;i++) {
		scanf("%d",&k);
		printf("%d\n",search(k));
	}
}
