#include <cstdio>
int coin[6] = {500,100,50,10,5,1};

int main()
{
	int pay,cnt=0;
	scanf("%d",&pay);
	pay = 1000 - pay;
	for(int i=0; i<6; ++i)
	{
		cnt += (pay / coin[i]);
		pay %= coin[i];
	}
	printf("%d\n",cnt);
}