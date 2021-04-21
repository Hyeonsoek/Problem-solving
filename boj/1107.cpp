#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#define abs(a) ((a)<0?(-(a)):(a))
using namespace std;
int broken[11]={};
int len,minx,s;

bool check(string s) {
	int slen = s.size();
	for(int i=0; i<slen; i++) {
		if(broken[s[i]-'0'])
			return false;
	}
	return true;
}

int main() {
	int n;
	scanf("%d%d",&s,&n);
	for(int i=0; i<n; i++) {
		int temp;
		scanf("%d",&temp);
		broken[temp]=1;
	}
	
	minx = abs(100-s);
	for(int i=0; i<1000000; i++) {
		string ss = to_string(i);
		int len_ss = ss.size();
		if(check(ss)) {
			minx = min(minx,len_ss+abs(i-s));
		}
	}
	printf("%d\n",minx);
}