//미완성

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

int n, m;
string board[10];

int bfs() {
    LOC red, blue;
    for(int i=0; i<n; i++) {
        for(int j=0; j<m; j++) {
            if (board[i][j] == 'R') {
                red = LOC(i, j);
                board[i][j] = '.';
            }
            if (board[i][j] == 'B') {
                blue = LOC(i, j);
                board[i][j] = '.';
            }
        }
    }

    bool check[10][10][10][10] = {};
    priority_queue<STATE> pq;

    pq.push(make_tuple(0, red, blue));
    check[red.first][red.second][blue.first][blue.second] = true;

    while (!pq.empty()) {
        STATE temp = pq.top();
        int cost = get<0>(temp);
        LOC rr = get<1>(temp);
        LOC bb = get<2>(temp);
        
        int ry = rr.first, rx = rr.second;
        int by = bb.first, bx = bb.second;

        // printf("(ry, rx) : (%d, %d), (by, bx) : (%d, %d)\n",ry, rx, by, bx);

        for(int i=0; i<4; i++) {
            int rmove = 0, rcheck = 0;
            int ryy = ry, rxx = rx;
            while (0 <= ryy < n && 0 <= rxx < m && board[ryy][rxx] == '.') {
                // printf("(ryy, rxx) : (%d, %d), (dy, dx) : (%d, %d) i : %d\n", ryy, rxx, dy[i], dx[i], i);
                rmove++;
                ryy += dy[i];
                rxx += dx[i];
                if(board[ryy][rxx] == 'O')
                    rcheck++;
            }

            if (board[ryy][rxx] == '#') {
                ryy -= dy[i];
                rxx -= dx[i];
            }

            int bmove = 0, bcheck = 0;
            int byy = by, bxx = bx;
            while (0 <= byy < n && 0 <= bxx < m && board[byy][bxx] == '.') {
                // printf("B\n");
                bmove++;
                byy += dy[i];
                bxx += dx[i];
                if(board[byy][bxx] == 'O')
                    bcheck++;
            }

            if(board[byy][bxx] == '#') {
                byy -= dy[i];
                bxx -= dx[i];
            }

            if (byy == ryy && bxx == rxx) {
                if(rmove > bmove) {
                    ryy -= dy[i];
                    rxx -= dx[i];
                }
                if(rmove < bmove) {
                    byy -= dy[i];
                    bxx -= dx[i];
                }
            }
            
            if (bcheck)
                continue;

            if (rcheck) {
                if (cost > 10)
                    continue;
                else return 1;
            }

            if (!check[ryy][rxx][byy][bxx]) {
                check[ryy][rxx][byy][bxx] = true;
                pq.push(make_tuple(cost + 1, LOC(ryy, rxx), LOC(byy, bxx)));
            }
            
        }
    }
    return 0;
}

int main()
{
    cin >> n >> m;
    for(int i=0; i<n; i++)
        cin >> board[i];

    printf("%d", bfs());

    return 0;
}
