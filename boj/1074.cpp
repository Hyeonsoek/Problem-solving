#include <cstdio>
#include <iostream>

void divide(int sx,int sy,int n,int r,int c,int temp) {
	if(n == 1) {
		for(int i=sx; i<sx+2; i++) {
			for(int j=sy; j<sy+2; j++) {
				if((r == i) && (c == j)) {
					printf("%d\n",temp);
					return;
				} temp++;
			}
		}
	}

	else {
		int k = (1 << (n-1)*2),f=0,t=(1<<n);
		for(int i=0; i<2; i++) {
			for(int j=0; j<2; j++) {
				if((r >= sx+(t/2)*i && c >= sy+(t/2)*j) &&
					(r < sx+(t/2)*(i+1) && c < sy+(t/2)*(j+1))) {
					divide(sx+(t/2)*i,sy+(t/2)*j,n-1,r,c,temp+f);
					return;
				} f+=k;
			}
		}
	}
}

int main() {
	int n,r,c;
	while(scanf("%d%d%d",&n,&r,&c)!=EOF) {
		divide(0,0,n,r,c,0);
	}
}
