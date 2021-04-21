#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
typedef vector<int> VEC;
int N,M,input[21],k=0;

void checker(VEC &v,int start,int cnt) {
	if(cnt == 0) {
		int temp = 0;
		int size = v.size();
		for(int i=0; i<size; i++) { temp += v[i]; }
		if(temp == M) k++;
	}
	else {
		for(int i=start; i<N; i++) {
			v.push_back(input[i]);
			checker(v,i+1,cnt-1);
			v.pop_back();
		}
	}
}

int main() {
	scanf("%d%d",&N,&M);
	for(int i=0; i<N; i++) {
		scanf("%d",&input[i]);
	} for(int i=1; i<=N; i++) {
		VEC v;
		checker(v,0,i);
	} printf("%d",k);
}
