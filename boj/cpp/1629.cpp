#include <cstdio>
#include <vector>

using namespace std;
long long A,B,C,sum=0;

long fast(long long A,int B)
{
	if(B==0) return 1;
	if(B==1) return A%C;
	if(B%2==0)
	{
		long N = fast((A*A)%C,B/2);
		return N;
	}
	else
	{
		long N = (A*fast((A*A)%C,(B-1)/2))%C;
		return N;
	}
}

int main() {
	scanf("%lld%lld%lld",&A,&B,&C);
	printf("%ld",fast(A,B));
}
