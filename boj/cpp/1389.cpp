#include <cstdio>
#include <queue>
#define INF (1<<31)-1
using namespace std;
typedef pair<int,int> p;
int n,user[101][101];
p mini = p(INF,101);

int bfs(int i) {
	int check[101]={},sum=0;
	queue <int> q;
	q.push(i);
	check[i] = 1;
	while(!q.empty()) {
		int x = q.front();
		q.pop();
		for(int j=1; j<=n; j++) {
			if(user[x][j] && !check[j]) {
				check[j] = check[x] + 1;
				q.push(j);
			}
		}
	}
	for(int j=1; j<=n; j++)
		sum += check[j];
	return sum-n;
}

int main() {
	int k;
	scanf("%d%d",&n,&k);
	for(int i=0; i<k; i++) {
		int x, y;
		scanf("%d%d",&x,&y);
		user[x][y] = user[y][x] = 1;
	}
	
	for(int i=1; i<=n; i++) {
		p temp = p(bfs(i),i);
		if(mini.first > temp.first) {
			mini = temp;
		}
	} printf("%d",mini.second);
}

