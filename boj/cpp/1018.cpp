#include <cstdio>
char map[51][51],chess[2]={'W','B'};
int n,m,min=65;

void checker(int sx,int sy) {
	if(sx + 8 > n) return;
	if(sx + 8 <= n && sy + 8 > m)
	{
		checker(sx+1,0);
		return;
	}

	if(sx + 8 <= n && sy + 8 <= m)
	{
		int check_1 = 0;
		int check_2 = 0;
		for(int i=sx; i<sx+8; i++) {
			for(int j=sy; j<sy+8; j++) {
				if(map[i][j] != chess[(i+j-sx-sy)%2]) {
					check_1++;
				}
			}
		}
		for(int i=sx; i<sx+8; i++) {
			for(int j=sy; j<sy+8; j++) {
				if(map[i][j] != chess[(i+j-sx-sy)%2==0]) {
					check_2++;
				}
			}
		}
		if(check_1 < min && check_2 < min) {
			if(check_1 < check_2) min = check_1;
			else min = check_2;
		} else if (check_1 < min && check_2 >= min) min = check_1;
        else if (check_2 < min && check_1 >= min) min = check_2;
		checker(sx,sy+1);
	}
}

int main() {
	scanf("%d%d",&n,&m);
	for(int i=0; i<n; i++) {
		scanf("%s",map[i]);
	} checker(0,0);
	printf("%d",min);
}
