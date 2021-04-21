#include <cstdio>
#include <cmath>
#include <cstdlib>
int main() {
	int T;
	scanf("%d",&T);
	for(int i=1; i<=T; i++) {
		int N,S,P,X,Y,sum=0;
		scanf("%d%d%d",&N,&S,&P);
		scanf("%d%d",&X,&Y);
		for(int i=0; i<N; i++) {
			int xx,yy;
			scanf("%d%d",&xx,&yy);
			sum+=abs(X-xx)+abs(Y-yy);
			X = xx,Y = yy;
		} sum *= S;
		printf("Data Set %d:\n",i);
		printf("%d\n\n",(int)ceil(sum/P+(sum%P!=0)));
	}
}

