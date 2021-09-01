#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
int nine[10];
typedef vector<int> VEC;
vector<VEC> vv;

void seven(VEC &v,int count,int start) {
	if(count == 0) {
		int temp = 0;
		for(int i=0; i<7; i++) { temp += v[i]; }
		if(temp == 100) {
			sort(v.begin(),v.end());
			vv.push_back(v);
			return;
		}
	}
	else {
		for(int i=start; i<9; i++) {
			v.push_back(nine[i]);
			seven(v,count-1,i+1);
			v.pop_back();
		}
	}
}

int main() {
	VEC v;
	for(int i=0; i<9; i++)
		scanf("%d",&nine[i]);
	seven(v,7,0);
	for(int i=0; i<7; i++) printf("%d\n",vv[0][i]);
}
