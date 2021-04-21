#include <cstdio>
using namespace std;
int n,dir[4][2] = {{1,0},{0,1},{-1,0},{0,-1}};
int maxi = 0;
char candy[51][51],color[4]={'C','P','Z','Y'};

void swap(char &a,char &b) {
	char temp = a;
	a = b;
	b = temp;
}

void find_max() {
	for(int i=0; i<4; i++) {
		int row[52][52]={};
		int colm[52][52]={};
		for(int j=0; j<n; j++) {
			for(int k=1; k<=n; k++) {
				if(color[i] == candy[j][k-1])
					row[j][k] = row[j][k-1]+1;
				if(maxi < row[j][k])
					maxi = row[j][k];
			}
		}
		for(int j=0; j<n; j++) {
			for(int k=1; k<=n; k++) {
				if(color[i] == candy[k-1][j])
					colm[k][j] = colm[k-1][j]+1;
				if(maxi < colm[k][j])
					maxi = colm[k][j];
			}
		}
	}
}

void solve(int sx,int sy) {
	if(sx == n-1 && sy == n-1)
		return;

	char &pre = candy[sx][sy];
	if(sy <= n-2) {
		char &next_row = candy[sx][sy+1];
		if(pre != next_row) {
			swap(pre,next_row);
			find_max();
			swap(pre,next_row);
		}
	}

	if(sx <= n-2) {
		char &next_colm = candy[sx+1][sy];
		if(pre != next_colm) {
			swap(pre,next_colm);
			find_max();
			swap(pre,next_colm);
		}
	}
	if(sy == n-1)
		solve(sx+1,0);
	if(sy < n-1)
		solve(sx,sy+1);
}

int main() {
	scanf("%d",&n);
	for(int i=0; i<n; i++)
		{ scanf("%s",candy[i]); }
	solve(0,0);
	printf("%d\n",maxi);
}
