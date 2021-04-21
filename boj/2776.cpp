#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int arr[1000001];
void bsearch(int start,int end,int find) {
	if(start > end) {
		printf("0\n");
		return;
	}
	else {
		int mid = (start+end)/2;
		if(arr[mid]==find) {
			printf("1\n");
			return;
		}
		if(arr[mid]>find)
			bsearch(start,mid-1,find);
		if(arr[mid]<find)
			bsearch(mid+1,end,find);
	}
}

int main() {
	int T;
	for(scanf("%d",&T);T--;) {
		int n,m;
		scanf("%d",&n);
		for(int i=0; i<n; i++)
			scanf("%d",&arr[i]);
		sort(arr,arr+n);
		scanf("%d",&m);
		for(int i=0; i<m; i++) {
			int temp;
			scanf("%d",&temp);
			bsearch(0,n,temp);
		}
		memset(arr,0,sizeof(arr));
	}
}
