// Online C++ compiler to run C++ program online
#include <iostream>

int main() {
    int n, m, b;
    int house[501][501] = {};
    
    scanf("%d%d%d", &n, &m, &b);
    for(int i=0; i<n; i++)
        for(int j=0; j<m; j++)
            scanf("%d", &house[i][j]);
    
    int tt = 1000000000, hh = 0;
    for(int h=0; h<257; h++)
    {
        int r = 0, c = 0;
        for(int i = 0; i < n; i++)
        {
            for(int j = 0; j < m; j++)
            {
                if (house[i][j] >= h)
                    r += house[i][j] - h;
                else c += h - house[i][j];
            }
        }
        
        if (b + r < c)
            continue;
        
        int t = r * 2 + c;
        if (tt >= t)
        {
            tt = t, hh = h;
        }
    }
    
    printf("%d %d", tt, hh);

    return 0;
}