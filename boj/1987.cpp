#include <cstdio>
#include <vector>
#include <queue>
using namespace std;
typedef vector<char> CHECK;
int N,M,maxi=0;
int dir[4][2] = {{1,0},{0,1},{-1,0},{0,-1}};
char string[21][21];

void dfs(CHECK &c,int sx,int sy) {
	int count=0;
	for(int i=0; i<26; i++) {
		if(c[i])
			count++;
	}
	if(count > maxi)
		maxi = count;
	for(int i=0; i<4; i++) {
		int xx = sx + dir[i][0];
		int yy = sy + dir[i][1];
		if(xx >= 0 && xx < N && yy >= 0 && yy < M && !c[string[xx][yy]-'A']) {
			c[string[xx][yy]-'A']=1;
			dfs(c,xx,yy);
			c[string[xx][yy]-'A']=0;
		}
	}
}

int main() {
	scanf("%d%d",&N,&M);
	for(int i=0; i<N; i++)
		scanf("%s",string[i]);
	CHECK c(26,0);
	c[string[0][0]-'A']=1;
	dfs(c,0,0);
	printf("%d\n",maxi);
}