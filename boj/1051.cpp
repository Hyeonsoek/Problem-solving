#include <cstdio>
using namespace std;

char input[51][51];
int digit[10],max=-1,N,M,size;
int sqare(int x,int y,int size) {
	if(size>1) {
		int cnt=0,temp=input[y][x]-'0';
		if(input[y+size-1][x]-'0'==temp) cnt++;
		if(input[y][x+size-1]-'0'==temp) cnt++;
		if(input[y+size-1][x+size-1]-'0'==temp) cnt++;
		if(cnt==3) return size*size;
		if(cnt<3) {
			if(x+size==M) {
				if (y+size==N) {
					return sqare(0,0,size-1);
				}else{
					return sqare(0,y+1,size);
				}
			} else {
				return sqare(x+1,y,size);
			}
		}
	} return 1;
}


int main() {
	scanf("%d%d",&N,&M);
	if(N>=M) size=M;
	else size=N;
	for(int i=0;i<N;i++){
		scanf("%s",input[i]);
		for(int j=0;j<M;j++){
			digit[input[i][j]-'0']++;
		}
	} int ss=size,s = sqare(0,0,ss);
	printf("%d",s);
}
