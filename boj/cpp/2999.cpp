#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;
typedef vector<vector<char> > matrix;
char input[101];

int main() {
	scanf("%s",input);
	int i,j,len = strlen(input);
	vector<int> v;
	for(int k=1; k<=len; k++) {
		if(len % k == 0) v.push_back(k);
	}
	if(v.size() % 2 == 0) { i = v[v.size()/2-1]; j = v[v.size()/2]; }
	else { i = v[v.size()/2]; j = v[v.size()/2]; }
	matrix a(i,vector<char>(j));
	for(int col=0; col<j; col++) {
		for(int row=0; row<i; row++) {
			a[row][col] = input[col*i+row];
		}
	} for(int row=0; row<i; row++) {
		for(int col=0; col<j; col++) {
			printf("%c",a[row][col]);
		}
	}
}
