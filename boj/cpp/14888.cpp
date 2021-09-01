#include <cstdio>
#include <vector>
#define MAX 1000000001
using namespace std;
vector<int> v(11);
int n;
int Max = -MAX,Min = MAX;

void brute(vector<int> &oper,int index,int sum)
{
	if(index == n-1)
	{
		if(sum < Min)
			Min = sum;
		if(sum > Max)
			Max = sum;
		return;
	}

	else
	{
		for(int i=0; i<4; ++i)
		{
			if(oper[i] > 0)
			{
				int temp = sum;
				switch(i)
				{
					case 0:
						sum += v[index+1];
						break;
					case 1:
						sum -= v[index+1];
						break;
					case 2:
						sum *= v[index+1];
						break;
					case 3:
						sum /= v[index+1];
						break;
				}
				--oper[i];
				brute(oper,index+1,sum);
				++oper[i];
				sum = temp;
			}
		}
	}
}

int main()
{
	scanf("%d",&n);

	vector<int> oper(5);
	for(int i=0; i<n; ++i)
		scanf("%d",&v[i]);

	for(int i=0; i<4; ++i)
		scanf("%d",&oper[i]);

	brute(oper,0,v[0]);
	printf("%d\n%d\n",Max,Min);
}