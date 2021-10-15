#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

struct state {
    int y, x;
};
const int dy[4] = {-1, 1, 0, 0};
const int dx[4] = {0, 0, -1, 1};

int n, m;
char board[50][50];

bool bound(int yy, int xx) {
    return 0 <= yy && yy < n && 0 <= xx && xx < m;
}

int bfs(int sy, int sx) {
    int answer = 0;
    int bmin = '9' + 1;
    int value = board[sy][sx];
    bool check[50][50] = {};
    queue<state> q;
    vector<state> v;

    q.push({sy, sx});
    v.push_back({sy, sx});
    check[sy][sx] = true;

    while (!q.empty()) {
        int y = q.front().y, x = q.front().x;
        q.pop();

        for(int i=0; i<4; i++) {
            int yy = y + dy[i];
            int xx = x + dx[i];
            if (bound(yy, xx) && !check[yy][xx]) {
                if (board[yy][xx] <= value) {
                    check[yy][xx] = true;
                    q.push({yy, xx});
                    v.push_back({yy, xx});
                } else
                    bmin = min(bmin, int(board[yy][xx]));
            }
        }
    }

    if (bmin == '9' + 1)
        return 0;

    for(auto loc : v) {
        int y = loc.y;
        int x = loc.x;
        if (y == 0 || y == n-1 || x == 0 || x == m-1)
            return 0;
    }

    for(auto loc : v) {
        int y = loc.y;
        int x = loc.x;
        answer += (bmin - board[y][x]);
        board[y][x] += (bmin - board[y][x]);
    }

    return answer;
}

int main() {
    cin >> n >> m;
    for(int i=0; i<n; i++)
        for(int j=0; j<m; j++)
            cin >> board[i][j];
    
    int answer = 0;
    for(int i=1; i<n-1; i++)
        for(int j=1; j<m-1; j++)
            answer += bfs(i, j);
    cout << answer;
}