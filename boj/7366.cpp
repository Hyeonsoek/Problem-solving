#include <cstdio>
#include <cstring>

int main() {
	char match[] = "sheep";
	int T,N,len;
	scanf("%d",&T);
	for(int t=0; t<T; t++) {
		int cnt = 0;
		char input[11][1001];
		scanf("%d",&N);
		for(int i=0; i<N; i++) {
			int check = 1;
			scanf("%s",input[i]);
			len = strlen(input[i]);
			if(len == 5) {
				for(int j=0; j<5; j++) {
					if(match[j] != input[i][j]) check = 0;
				} if(check == 1) cnt++;
			}
		} printf("Case %d: This list contains %d sheep.\n\n",t+1,cnt);
	}
}
