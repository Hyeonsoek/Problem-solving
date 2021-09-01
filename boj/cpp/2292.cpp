#include <cstdio>

int main()
{
	int input;
	scanf("%d",&input);

	int cnt = 1;
	long long range = 1;
	long long temp = 1;

	while(range < input)
	{
		temp = 6*(cnt++);
		range += temp;
	}

	printf("%d",cnt);
}