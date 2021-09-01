#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
typedef vector<char> VEC;
int L,C;
VEC v;
char *vowel="aeiou";
char *consn="bcdfghjklmnpqrstvwxyz";

void solve(VEC &pre,int s,int cnt) {
	if(cnt == 0) {
		int vv=0,cc=0;
		for(int i=0; i<pre.size(); i++) {
			for(int j=0; j<5; j++) {
				if(pre[i]==vowel[j]) vv++;
			}
			for(int j=0; j<21; j++) {
				if(pre[i]==consn[j]) cc++;
			}
		}

		if(cc > 1 && vv > 0) {
			for(int i=0; i<pre.size(); i++)
				printf("%c",pre[i]);
			printf("\n");
		}return;
	}
	for(int i=s; i<C; i++) {
		pre.push_back(v[i]);
		solve(pre,i+1,cnt-1);
		pre.pop_back();
	}
}

int main() {
	scanf("%d%d",&L,&C);
	for(int i=0; i<C; i++) {
		char a; scanf(" %c",&a);
		v.push_back(a);
	} sort(v.begin(),v.end());
	VEC a;
	solve(a,0,L);
}
