#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <iostream>
#include <cstdlib>
#include <queue>
#define MAX 10000
using namespace std;
typedef string vec;
typedef pair<int,vec> p;

void bfs() {
	queue<p> q;
	int check[10001]={};
	int end,start;
	scanf("%d%d",&start,&end);
	q.push(p(start,""));
	check[start]=1;
	while(!q.empty()) {
		int value = q.front().first;
		vec pre = q.front().second;
		q.pop();
		if(value == end) {
			cout << pre << endl;
			break;
		}
		int S = (MAX+value-1)%MAX;
		if(!check[S]) {
			check[S]=1;
			q.push(p(S,pre+"S"));
		}
		int D = (value*2)%MAX;
		if(!check[D]) {
			check[D]=1;
			q.push(p(D,pre+"D"));
		}
		int left = value/1000 + (value%1000)*10;
		if(!check[left]) {
			check[left]=1;
			q.push(p(left,pre+"L"));
		}
		int right = value/10 + (value%10)*1000;
		if(!check[right]) {
			check[right]=1;
			q.push(p(right,pre+"R"));
		}
	}
}

int main() {
	int T;
	scanf("%d",&T);
	for(int i=0; i<T; i++) {
		bfs();
	}
}