#include <cstdio>
#include <queue>
#include <tuple>
#include <cstring>
#include <string>
#include <iostream>
using namespace std;
typedef tuple< int,int,int > t;

void BFS(int L,int R,int C) {
	t end;
	queue< t > q;
	string s;
	char map[51][51][51] = {};
	int check[51][51][51] = {};
	memset(check,0,sizeof(check));
	int dir[6][3] = {{0,0,1},{0,0,-1},{0,1,0},{0,-1,0},{1,0,0},{-1,0,0}};
	for(int i = 0; i < L; i++) {
		for(int j = 0; j < R; j++) {
			scanf("%s",map[i][j]);
			for(int k = 0; k < C; k++) {
				if(map[i][j][k] == 'S') {
					q.push(t(i,j,k));
					check[i][j][k]=1;
				}
				if(map[i][j][k] == 'E')
					end = t(i,j,k);
			}
		}
		getline(cin,s);
	}
	while(!q.empty()) {
		int z = get<0>(q.front());
		int y = get<1>(q.front());
		int x = get<2>(q.front());
		if (map[z][y][x]=='E')
			break;
		q.pop();
		for (int i = 0; i < 6; i++) {
			int zz = z + dir[i][0];
			int yy = y + dir[i][1];
			int xx = x + dir[i][2];
			if(xx<0 || xx>=C || yy<0 || yy>=R || zz<0 || zz>=L)
				continue;
			if(map[zz][yy][xx] == '#' || check[zz][yy][xx])
				continue;
			check[zz][yy][xx] = check[z][y][x] + 1;
			q.push(t(zz,yy,xx));
		}
	}
	if (check[get<0>(end)][get<1>(end)][get<2>(end)] == 0)
		printf("Trapped!\n");
	else
		printf("Escaped in %d minute(s).\n",check[get<0>(end)][get<1>(end)][get<2>(end)]-1);
}

int main() {
	int L,R,C;
	scanf("%d%d%d",&L,&R,&C);
	while(L!=0 || R!=0 || C!=0)
	{
		BFS(L,R,C);
		scanf("%d%d%d",&L,&R,&C);
	}
}
