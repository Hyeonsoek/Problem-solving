#include <cstdio>

int first[6] = {500,300,200,50,30,10};
int second[5] = {512,256,128,64,32};

int find1(int a)
{
	int i=1,pos=0;
	while(a>0)
		a-= (i++),pos++;
	return pos;
}

int find2(int b)
{
	int i=1,pos=0;
	while(b>0)
		b-= i,pos++,i*=2;
	return pos;	
}

int main()
{
	int T;
	for(scanf("%d",&T);T>0;--T)
	{
		int a,b;
		scanf("%d%d",&a,&b);
		int posa=find1(a);
		int posb=find2(b);

		int ans = 0;
		ans += posa > 6 ? 0 : first[posa-1];
		ans += posb > 5 ? 0 : second[posb-1];
		printf("%d\n",ans*10000);
	}
}