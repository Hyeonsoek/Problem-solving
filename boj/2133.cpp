#include <cstdio>
#include <cmath>

int main() {
	int n,d[31] = {1,0,3};
	scanf("%d",&n);
	for(int i=4; i<=n; i+=2)
	{
		d[i] = d[i-2] * 3;
		for(int j=4; j<=i; j+=2)
			d[i] += d[i-j] * 2;
	}
	printf("%d\n",d[n]);
	return 0;
}