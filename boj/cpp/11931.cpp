#include <cstdio>
#include <algorithm>
#define MAX 1000000
using namespace std;
int n;
vector<int> v;

int main() {
	scanf("%d",&n);
	for(int i=0; i<n; i++) {
		int input;
		scanf("%d",&input);
		v.push_back(input);
	} sort(v.begin(),v.end(),greater<int>());
	for(int i=0; i<n; i++) printf("%d\n",v[i]);
}
