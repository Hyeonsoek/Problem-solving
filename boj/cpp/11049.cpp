#include <cstdio>
#define MAX (1<<31)-1
#define min(a,b) (a>b?b:a)
int d[501];
int M[501][501];
void minmult(int n)
{
	int j,k,diag;
	for(int i=0; i<=n; i++)
	{
		for(int j=0; j<=n; j++)
			M[i][j]=MAX;
		M[i][i]=0;
	}
	for(diag = 1; diag <= n-1; diag++)
		for(int i=1; i<=n-diag; i++)
		{
			j = i+diag;
			for(int k=i; k<=j-1; k++)
				M[i][j] = min(M[i][j],M[i][k]+M[k+1][j]+
					d[i-1]*d[k]*d[j]);
		}
}

int main(){
	int n;
	scanf("%d",&n);
	for(int i=0; i<n; ++i)
		scanf("%d%d",&d[i],&d[i+1]);
	minmult(n);
	printf("%d\n",M[1][n]);
}