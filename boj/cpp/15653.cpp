#include <utility>
#include <queue>
#include <tuple>
#include <algorithm>
#include <iostream>
using namespace std;

typedef pair<int, int> LOC;
typedef tuple<int, LOC, LOC> STATE;

int dy[4] = {-1, 1, 0, 0};
int dx[4] = {0, 0, -1, 1};
bool check[10][10][10][10];

int n, m;
char board[10][10];

void move(int &y, int &x, int &move, int dy, int dx) {
    while (board[y+dy][x+dx] != '#' && board[y][x] != 'O') {
        move += 1;
        y += dy;
        x += dx;
    }
}

int bfs() {
    LOC red, blue;
    for(int i=0; i<n; i++) {
        for(int j=0; j<m; j++) {
            if (board[i][j] == 'R')
                red = LOC(i, j);
            if (board[i][j] == 'B')
                blue = LOC(i, j);
        }
    }

    queue<STATE> q;

    q.push(make_tuple(0, red, blue));
    check[red.first][red.second][blue.first][blue.second] = true;

    while (!q.empty()) {
        STATE temp = q.front();
        int cost = get<0>(temp);
        LOC rr = get<1>(temp);
        LOC bb = get<2>(temp);

        q.pop();
        
        int ry = rr.first, rx = rr.second;
        int by = bb.first, bx = bb.second;

        for(int i=0; i<4; i++) {
            int rmove = 0, ryy = ry, rxx = rx;
            int bmove = 0, byy = by, bxx = bx;
            
            move(ryy, rxx, rmove, dy[i], dx[i]);
            move(byy, bxx, bmove, dy[i], dx[i]);

            if (board[byy][bxx] == 'O')
                continue;

            if (board[ryy][rxx] == 'O')
                return cost+1;

            if (byy == ryy && bxx == rxx) {
                if(rmove > bmove) {
                    ryy -= dy[i];
                    rxx -= dx[i];
                }
                else {
                    byy -= dy[i];
                    bxx -= dx[i];
                }
            }

            if (!check[ryy][rxx][byy][bxx]) {
                check[ryy][rxx][byy][bxx] = true;
                q.push(make_tuple(cost + 1, LOC(ryy, rxx), LOC(byy, bxx)));
            }
            
        }
    }
    return -1;
}

int main()
{
    cin >> n >> m;
    for(int i=0; i<n; i++)
        for(int j=0; j<m; j++)
            cin >> board[i][j];

    printf("%d\n", bfs());

    return 0;
}