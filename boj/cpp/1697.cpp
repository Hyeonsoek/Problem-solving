#include <cstdio>
#include <queue>
using namespace std;
int check[100003];
void bfs(int N,int M) {
	queue<int> q;
	q.push(N);
	check[N]=1;
	while (!q.empty()) {
		int x = q.front();
		q.pop();
		if (x==M) break;
		if (x-1>=0&&!check[x-1]) {
			check[x-1]=check[x]+1;
			q.push(x-1);
		} if (x+1<=100000&&!check[x+1]) {
			check[x+1]=check[x]+1;
			q.push(x+1);
		} if (x*2<=100000&&!check[x*2]) {
			check[x*2]=check[x]+1;
			q.push(x*2);
		}
	} printf("%d",check[M]-1);
}
int main() {
	int N,M;
	scanf("%d%d",&N,&M);
	bfs(N,M);
}
