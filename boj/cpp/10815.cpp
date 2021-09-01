#include <cstdio>
#include <algorithm>
using namespace std;
int N1,N2,deck1[500001],deck2;
int bsearch(int start,int end,int num) {
	int mid = (start + end)/2;
	if (start>end) return 0;
	if (deck1[mid] == num) return 1;
	if (deck1[mid] > num) return bsearch(start,mid-1,num);
	if (deck1[mid] < num) return bsearch(mid+1,end,num);
}

int main() {
	scanf("%d",&N1);
	for (int i = 0; i < N1; i++)
		scanf("%d",&deck1[i]);
	sort(deck1,deck1+N1);
	scanf("%d",&N2);
	for (int i = 0; i < N2; i++) {
		scanf("%d",&deck2);
		printf("%d ",bsearch(0,N1,deck2));
	}
}
