#include <cstdio>

int main()
{
	int n;
	int room[1000003] = {};
	scanf("%d",&n);

	for(int i=0; i<n; ++i)
		scanf("%d",&room[i]);

	int count = 0;
	for(int i=0; i<n; ++i)
	{
		if(room[i] == 1)
		{
			count++;
			room[i+1] =! room[i+1];
			room[i+2] =! room[i+2];
		}
	}
	printf("%d\n",count);
}