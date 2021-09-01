#include <cstdio>
char input[65][65];
int N;
void divide(int n,int x,int y) {
	char first = input[x][y];
	int count = 0;
	for (int i = x; i < x+n; i++) {
		for (int j = y; j < y+n; j++) {
			if (input[i][j] != first) {
				break;
			} else count++;
		}
	} if (count != n*n) {
		printf("(");
	} else {printf("%c",first); return;}
	if (n/2 != 0) {
		divide(n/2,x,y);
		divide(n/2,x,y+n/2);
		divide(n/2,x+n/2,y);
		divide(n/2,x+n/2,y+n/2);
		printf(")");
	}
}

int main() {
	scanf("%d",&N);
	for (int i = 0; i < N; i++)
		scanf("%s",input[i]);
	divide(N,0,0);
}
