#include <cstdio>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;
vector <int> v;
int check[26][26],N,dir[4][2]={{0,1},{0,-1},{1,0},{-1,0}};
char map[26][26];

void bfs(int i,int j) {
	int count=0;
	queue< pair<int,int> > q;
	q.push(make_pair(i,j));
	check[i][j]=1;
	while (!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		count++;
		q.pop();
		for (int i=0; i<4; i++) {
			int xx = x + dir[i][0];
			int yy = y + dir[i][1];
			if (xx>=0 && xx<N && yy>=0 && yy<N
					&& !check[xx][yy] && map[xx][yy]!='0') {
				check[xx][yy]=check[x][y]+1;
				q.push(make_pair(xx,yy));
			}
		}
	} v.push_back(count);
}
int main() {
	scanf("%d",&N);
	for (int i=0;i<N;i++){
		scanf("%s",map[i]);
	} for (int i=0;i<N;i++){
		for (int j=0;j<N;j++){
			if(map[i][j]=='1'&&!check[i][j]) {
				bfs(i,j);
			}
		}
	} printf("%d\n",v.size());
	sort(v.begin(),v.end());
	for (int i = 0; i < v.size(); i++) {
		printf("%d\n",v.at(i));
	}
}
