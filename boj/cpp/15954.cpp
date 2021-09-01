#include <cstdio>
#include <cmath>

int main()
{
	int N,K;
	long double min = 1.79E+307;
	int doll[501] = {};
	scanf("%d%d",&N,&K);
	for(int i=0; i<N; ++i)
		scanf("%d",&doll[i]);

	for(int i=0; i<N; ++i)
	{
		for(int k=K; k+i<=N; ++k)
		{
			long double avg = 0;
			long double sigma = 0;
			for(int j=i; j<i+k; ++j)
				avg += doll[j];
			avg /= k;

			for(int j=i; j<i+k; ++j)
				sigma += pow((doll[j]-avg),2);
			sigma /= k;
			sigma = sqrt(sigma);
			if(min > sigma)
				min = sigma;
		}
	}
	printf("%.10Lf\n",min);
}