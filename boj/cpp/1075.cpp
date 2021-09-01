#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
using namespace std;
int main() {
	int N,F;
	scanf("%d%d",&N,&F);
	string s = to_string(N);
	for(int i=0; i<10; i++) {
		for(int j=0; j<10; j++) {
			s[s.size()-2] = i+'0';
			s[s.size()-1] = j+'0';
			int K = atoi(s.c_str());
			if(K % F == 0) {
				cout << s.substr(s.size()-2,s.size());
				return 0;
			}
		}
	}
}
