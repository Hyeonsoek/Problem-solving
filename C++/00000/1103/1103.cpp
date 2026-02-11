#include <bits/stdc++.h>
using namespace std;

int drx[] = {-1, 1, 0, 0};
int dry[] = {0, 0, -1, 1};

int n, m, h;
int cache[51][51];

bool isLoop;
bool visited[51][51];
string board[51];

int dynamic(int x, int y)
{
	if (visited[y][x])
	{
		isLoop = true;
		return 0;
	}

	if (board[y][x] == 'H')
		return 0;

	int j = board[y][x] - '0';
	int &ret = cache[y][x];
	if (ret != -1)
		return ret;

	visited[y][x] = true;

	ret = 1;
	for (int i = 0; i < 4; i++)
	{
		int xx = x + j * drx[i];
		int yy = y + j * dry[i];
		if (xx < 0 || xx >= m || yy < 0 || yy >= n)
			continue;

		ret = max(ret, 1 + dynamic(xx, yy));
	}

	visited[y][x] = false;
	return ret;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> m;
	for (int i = 0; i < n; i++)
		cin >> board[i];

	memset(cache, -1, sizeof(cache));

	int res = dynamic(0, 0);
	cout << (isLoop ? -1 : res);
}