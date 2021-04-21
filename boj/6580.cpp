#include <stdio.h>
char map[513][513];
int N,M;


void dq(int sx,int sy,int size) {
	int temp = map[sx][sy],check=0;
	for(int i=sx; i<sx+size; i++) {
		for(int j=sy; j<sy+size; j++) {
			if(temp!=map[i][j]) {
				check=1;
			}
		}
	} if(check==0) {
		printf("%c",temp);
		return;
	} else {
		printf("Q");
		dq(sx,sy,size/2);
		dq(sx,sy+size/2,size/2);
		dq(sx+size/2,sy,size/2);
		dq(sx+size/2,sy+size/2,size/2);
	}
}
int main() {
	scanf("%*s%*s%d",&N);
	scanf("%*s%*s%d",&M);
	scanf("%*s%*s%*s%*s%*s");
	for(int i=0; i<N; i++) {
		for(int j=0; j<N/8; j++) {
			int temp=128,num,k=7;
			scanf("%x,",&num);
			while(temp!=0) {
				if(temp<=num){
					map[i][j*8+(k--)]='B';
					num-=temp;
				} else {
					map[i][j*8+(k--)]='W';
				} temp/=2;
			}
		}
	} scanf("%*s");
	printf("%d\n",N);
	dq(0,0,N);
}
