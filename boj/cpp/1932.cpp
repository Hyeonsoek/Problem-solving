#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int map[501][501];
int check[501][501];
int n;

int solve(int i,int j) {
	if(i > n || j > n) return 0;
	int &ret = check[i][j];
	if(ret != -1) return ret;
	ret = map[i][j];
	if(i+1 <= n && j+1 <= n) {
		ret += max(solve(i+1,j),solve(i+1,j+1));
	}
	if(ret == -1)
		return 0;
	else return ret;
}

int main() {
	scanf("%d",&n);
	memset(check,-1,sizeof(check));
	for(int i=0; i<=n; i++) {
		for(int j=0; j<i; j++)
			scanf("%d",&map[i][j]);
	}
	printf("%d",solve(0,0));
}
