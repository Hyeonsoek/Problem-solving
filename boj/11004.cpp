#include <cstdio>
#include <algorithm>
using namespace std;
int map[5000001];
int main() {
	int n,k;
	scanf("%d%d",&n,&k);
	for(int i=0; i<n; i++)
		scanf("%d",&map[i]);
	sort(map,map+n);
	printf("%d",map[k-1]);
}