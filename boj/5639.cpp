#include <cstdio>
#include <vector>
using namespace std;
vector<int> temp;

void recursion(int start,int end) {
	int slice=-1;
	int len = end - start + 1;
	for(int i=start; i <= end; ++i) {
		if(temp[start] < temp[i]) {
			slice = i;
			break;
		}
	}
	if(slice != -1) {
		recursion(start+1,slice-1);
		recursion(slice,end);
	}
	else {
		if(len > 1)
			recursion(start+1,end);
	}
	if(len != 0)
		printf("%d\n",temp[start]);
}

int main() {
	for(int s;scanf("%d",&s)!=EOF;temp.push_back(s));
	recursion(0,temp.size()-1);
}
