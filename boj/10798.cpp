#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;
int main() {
	vector<vector<char> > VEC(15,vector<char>());
	for(int i=0; i<5; i++) {
		char input[16]={};
		scanf("%s",input);
		for(int j=0; j<strlen(input); j++) {
			VEC[j].push_back(input[j]);
		}
	}
	for(int i=0; i<15; i++) {
		int len = VEC[i].size();
		for(int j=0; j<len; j++) {
			printf("%c",VEC[i][j]);
		}
	}
}
