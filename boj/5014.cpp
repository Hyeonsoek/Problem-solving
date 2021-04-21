#include <cstdio>
#include <queue>
using namespace std;
int f,s,g,u,d;
int check[1000002];

void bfs(int s) {
	queue <int> q;
	q.push(s);
	check[s] = 1;
	while(!q.empty()) {
		int x = q.front();
		if(x == g) break;
		q.pop();
		if(x+u <= f && !check[x+u]) {check[x+u]=check[x]+1; q.push(x+u);}
		if(x-d > 0 && !check[x-d]) {check[x-d]=check[x]+1; q.push(x-d);}
	} 
	if(check[g]!=0) printf("%d",check[g]-1);
	else printf("use the stairs");
}

int main() {
	scanf("%d%d%d%d%d",&f,&s,&g,&u,&d);
	bfs(s);
}