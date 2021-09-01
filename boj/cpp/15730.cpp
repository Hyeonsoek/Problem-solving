#include <queue>
#include <cstdio>
#include <utility>
#include <vector>
#include <algorithm>
using namespace std;

typedef pair<int,int> P;

int n,m;
int dir[4][2] = {{1,0},{0,1},{-1,0},{0,-1}};
int san[101][101];

bool compare(const P &a ,const P &b)
{
	return san[a.first][a.second] < san[b.first][b.second];
}

int bfs()
{
	vector< P > in;
	for(int i=1; i<n-1; ++i)
		for(int j=1; j<m-1; ++j)
			in.push_back(P(i,j));

	int size = in.size();
	sort(in.begin(),in.end(),compare);

	int cost = 0;
	for(int i=0; i<size; ++i)
	{
		int talju = 0;
		vector< P > idx;
		queue< P > bfs;
		vector< vector<int> > check(n,vector<int>(m,0));
		
		idx.push_back(in[i]);
		bfs.push(in[i]);
		check[in[i].first][in[i].second] = 1;

		int min = 10001;
		while(!bfs.empty())
		{
			int x = bfs.front().first;
			int y = bfs.front().second;

			bfs.pop();

			for(int j=0; j<4; j++)
			{
				int xx = x + dir[j][0];
				int yy = y + dir[j][1];

				if(xx >=0 && xx < n && yy >= 0 && yy < m)
				{

					if(!check[xx][yy] && (san[xx][yy] == san[x][y]))
					{
						if(xx == 0 || xx == n-1 || yy == 0 || yy == m-1)
						{ talju = 1; break; }
						check[xx][yy] = 1;
						idx.push_back(P(xx,yy));
						bfs.push(P(xx,yy));
						continue;
					}
					if(san[xx][yy] != san[x][y] && san[xx][yy] < min)
						min = san[xx][yy];
				}
			}
		}

		if(talju || min == 10001)
			continue;

		if(min > san[in[i].first][in[i].second])
		{
			int idxsize = idx.size();
			int gap = min - san[in[i].first][in[i].second]; 
			cost += gap * idxsize;

			for(int i=0; i<idxsize; ++i)
			{
				P &p = idx[i];
				san[p.first][p.second] += gap;
			}
		}
	}

	return cost;
}

int main()
{
	scanf("%d%d",&n,&m);
	for(int i=0; i<n; ++i)
		for(int j=0; j<m; ++j)
			scanf("%d",&san[i][j]);

	printf("%d\n",bfs());
}