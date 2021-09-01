#include <cstdio>
#include <cmath>
#include <queue>
using namespace std;
struct Tree
{
	int root=-1,left=-1,right=-1;
	int lidx=-1,ridx=-1;
}t[1025];

int height,size,node[1025];

void find_tree(int breath,int n,int start,int last)
{
	if(n > start && n < last-1)
	{
		int temp = breath;
		if(n - temp >= start) {
			t[n].left = t[n-temp].root;
			t[n].lidx = n-temp;
			find_tree(breath/2,n-temp,0,n);
		}
		if(temp + n < last) {
			t[n].right = t[n+temp].root;
			t[n].ridx = n+temp;
			find_tree(breath/2,n+temp,n,last);
		}
	}
}

bool check_num(int num) {
	int n = 1;
	while(num != 0) {
		if(num < 0) { return false; }
		num -= n;
		n *= 2;
	} return true;
}


int bfs(int n) {
	queue<int> q;
	q.push(n);
	int check[1025]={},cnt=0;
	while(!q.empty()) {
		int idx = q.front();cnt++;
		printf("%d ",t[idx].root);
		if(check_num(cnt)) printf("\n");
		q.pop();
		if(t[idx].lidx != -1) {
			check[t[idx].lidx] = 1;
			q.push(t[idx].lidx);
		} if(t[idx].right != -1) {
			check[t[idx].right] = 1;
			q.push(t[idx].ridx);
		}
	}
}


int main()
{
	scanf("%d",&height);
	size = (1<<height) - 1;
	if(height > 1) {
		height = (1<<(height-2)) - 1;
		for(int i=0; i<(1<<height)-1; i++) {
			scanf("%d",&node[i]);
			t[i].root = node[i];
		}
		find_tree(height,size/2,0,size);
		bfs(size/2);
	} else {
		int temp;
		scanf("%d",&temp);
		printf("%d",temp);
	}
}