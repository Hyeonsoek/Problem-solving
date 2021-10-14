#include <vector>
#include <utility>
#include <iostream>
#include <algorithm>
using namespace std;

int n;
int matter[10][4][4];
char matterC[10][4][4];
int dy[4] = {0, 1, 0, 1};
int dx[4] = {0, 0, 1, 1};

void product(vector<int> &o, vector<vector<int> > &store) {
    if(o.size() == 3) {
        store.push_back(o);
    } else {
        for(int i=0; i<4; i++) {
            o.push_back(i);
            product(o, store);
            o.pop_back();
        }
    }
}

void permutaiton(vector<int>& o, vector<vector<int> > &store, vector<int> &check) {
    if( o.size() == 3) {
        store.push_back(o);
    } else {
        for(int i=0; i<n; i++) {
            if( !check[i] ) {
                check[i] = 1;
                o.push_back(i);
                permutaiton(o, store, check);
                o.pop_back();
                check[i] = 0;
            }
        }
    }
}

pair<int, int> now_location(int y, int x, int rotate) {
    switch (rotate)
    {
        case 0:
            return make_pair(y, x);
        case 1:
            return make_pair(x, 3-y);
        case 2:
            return make_pair(3-y, 3-x);
        case 3:
            return make_pair(3-x, y);
    }
}

int alchemy(vector<int> order, vector<int> rotate, vector<int> start) {
    int board[5][5];
    char boardC[5][5];

    for(int i=0; i<5; i++) {
        for(int j=0; j<5; j++) {
            board[i][j] = 0;
            boardC[i][j] = 'W';
        }
    }

    // printf("START\n");
    for(int i=0; i<3; i++) {
        for(int j=0; j<4; j++) {
            for(int k=0; k<4; k++) {
                pair<int, int> p = now_location(j, k, rotate[i]);
                int yy = p.first + dy[start[i]], xx = p.second + dx[start[i]];
                // printf("\t(yy, xx): (%d, %d), (j, k) = (%d, %d), r = %d, s = %d\n", yy, xx, j, k, rotate[i], start[i]);
                board[yy][xx] += matter[order[i]][j][k];
                if(board[yy][xx] < 0)
                    board[yy][xx] = 0;
                else if(board[yy][xx] > 9)
                    board[yy][xx] = 9;

                if (matterC[order[i]][j][k] != 'W')
                    boardC[yy][xx] = matterC[order[i]][j][k];
            }
        }
    }

    int answer = 0;
    for(int i=0; i<5; i++) {
        for(int j=0; j<5; j++) {
            switch (boardC[i][j])
            {
                case 'R':
                    answer += (board[i][j] * 7);
                    break;
                case 'B':
                    answer += (board[i][j] * 5);
                    break;
                case 'G':
                    answer += (board[i][j] * 3);
                    break;
                case 'Y':
                    answer += (board[i][j] * 2);
                    break;
                default:
                    break;
            }
        }
    }

    return answer;
}

int main()
{
    cin >> n;
    for(int i=0; i<n; i++) {
        for(int j=0; j<4; j++)
            for(int k=0; k<4; k++)
                cin >> matter[i][j][k];
        for(int j=0; j<4; j++)
            for(int k=0; k<4; k++)
                cin >> matterC[i][j][k];
    }


    // order 구했음!
    vector<int> temp;
    vector<vector<int> > order, rotation;
    vector<int> check(n, 0);
    permutaiton(temp, order, check);
    product(temp, rotation);

    int maxValue = 0;
    int orderSize = order.size();
    int rotationSize = rotation.size();
    for(int i=0; i<orderSize; i++)
        for(int j=0; j<rotationSize; j++)
            for(int k=0; k<rotationSize; k++)
                maxValue = max(alchemy(order[i], rotation[j], rotation[k]), maxValue);
    
    printf("%d",maxValue);
    
    return 0;
}
