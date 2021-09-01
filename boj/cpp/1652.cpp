#include <cstdio>

int main() {
	int N,cnt=0,cnt_w=0,cnt_h=0; char map[101][101]={};
	scanf("%d",&N);
	for(int i=0; i<N; i++) {
		scanf("%s",map[i]);
		for(int j=0; j<N; j++) {
			if(map[i][j] == 'X') {
				if(cnt >= 2) {cnt_w++;}
				cnt = 0;
			}

			if(map[i][j] == '.') {
				cnt++;
				if(j == N-1 && cnt >= 2) cnt_w++;
			}
		} cnt = 0;
	}

	for(int i=0; i<N; i++) {
		for(int j=0; j<N; j++) {
			if(map[j][i] == 'X') {
				if(cnt >= 2) {cnt_h++;}
				cnt=0;
			}
			
			if(map[j][i] == '.') {
				cnt++;
				if(j == N-1 && cnt >= 2) cnt_h++;
			}
		} cnt=0;
	}

	printf("%d %d",cnt_w,cnt_h);
}
