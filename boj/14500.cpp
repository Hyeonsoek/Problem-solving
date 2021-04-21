#include <cstdio>
#include <vector>
#include <utility>
using namespace std;

int N,M,Max=-1;
vector<vector<int> > Map(501,vector<int>(501));
int Tetromino[19][4][2] = {
    {{0, 0}, {1, 0}, {2, 0}, {3, 0}},
    {{0, 0}, {0, 1}, {0, 2}, {0, 3}},
    {{0, 0}, {0, 1}, {1, 0}, {1, 1}},
    {{0, 0}, {1, 0}, {2, 0}, {2, 1}},
    {{0, 0}, {1, -2}, {1, -1}, {1, 0}},
    {{0, 0}, {0, 1}, {1, 1}, {2, 1}},
    {{0, 0}, {0, 1}, {0, 2}, {1, 0}},
    {{0, 0}, {1, 0}, {2, 0}, {2, -1}},
    {{0, 0}, {0, 1}, {0, 2}, {1, 2}},
    {{0, 0}, {0, 1}, {1, 0}, {2, 0}},
    {{0, 0}, {1, 0}, {1, 1}, {1, 2}},
    {{0, 0}, {1, 0}, {1, 1}, {2, 1}},
    {{0, 0}, {0, 1}, {1, -1}, {1, 0}},
    {{0, 0}, {1, -1}, {1, 0}, {2, -1}},
    {{0, 0}, {0, 1}, {1, 1}, {1, 2}},
    {{0, 0}, {0, 1}, {0, 2}, {1, 1}},
    {{0, 0}, {1, 0}, {1, 1}, {2, 0}},
    {{0, 0}, {1, -1}, {1, 0}, {1, 1}},
    {{0, 0}, {1, -1}, {1, 0}, {2, 0}},
};

void brute(int y,int x,int count,int sum)
{
	for(int i=0; i<19; ++i)
	{
		bool check = true;
		int sum = 0;
		for(int j=0; j<4; ++j)
		{
			int yy = y + Tetromino[i][j][0];
			int xx = x + Tetromino[i][j][1];
			if(yy >= 0 && yy < N && xx >= 0 && xx < M)
				sum += Map[yy][xx];
			else
				{ check = false; break; }
		}
		if(check && sum > Max)
			Max = sum;
	}
}
int main()
{
	scanf("%d%d",&N,&M);
	for(int i=0; i<N; ++i)
		for(int j=0; j<M; ++j)
			scanf("%d",&Map[i][j]);

	for(int i=0; i<N; ++i)
		for(int j=0; j<M; ++j)
			brute(i,j,3,Map[i][j]);
	printf("%d\n",Max);
}