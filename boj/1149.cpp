#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int map[1001][3];
int check[1001][3];
int N,m=(1<<30)-1;

int solve(int x,int y,int van) {
	if(x >= N) return 0;
	int &ret = check[x][y];
	if(ret != -1)
		return ret;
	int m = map[x][y];
	if(van == 0)
		ret = m + min(solve(x+1,1,1),solve(x+1,2,2));
	if(van == 1)
		ret = m + min(solve(x+1,0,0),solve(x+1,2,2));
	if(van == 2)
		ret = m + min(solve(x+1,0,0),solve(x+1,1,1));
	return ret;
}

int main() {
	scanf("%d",&N);
	for(int i=0; i<N; i++) {
		for(int j=0; j<3; j++)
			scanf("%d",&map[i][j]);
	}
	for(int i=0; i<3; i++) {
		memset(check,-1,sizeof(check));
		int t = solve(0,i,i);
		if(m > t) m = t;
	}
	printf("%d",m);
}