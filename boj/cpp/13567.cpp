#include <cstdio>

int main() {
	int M,N,dir[4][2] = {{1,0},{0,1},{-1,0},{0,-1}};
	int x = 0, y = 0;
	int idx = 0,check=1;
	scanf("%d%d",&M,&N);
	for(int i=0; i<N; i++) {
		int temp;
		char input[5];
		scanf("%s%d",input,&temp);
		if(check) {
			if(input[0] == 'M') {
				x += temp * dir[idx][0];
				y += temp * dir[idx][1];
				if(x >= 0 && x <= M && y >=0 && y <= M);
				else check = 0;
			}
			if(input[0] == 'T') {
				if(temp == 0) {
					idx += 1;
					if(idx == 4) idx -= 4;
				} else {
					idx-=1;
					if(idx == -1) idx += 4;
				}
			}
		}
	}

	if(check) printf("%d %d",x,y);
	else printf("-1");
}
