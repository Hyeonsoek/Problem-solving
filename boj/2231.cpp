#include <cstdio>
#include <vector>
#include <string>
using namespace std;
vector<int> hap(1000200);

int main()
{
	for(int i=1; i<1000001; ++i)
	{
		int sang = i;
		string temp = to_string(i);
		for(int j=0; j<temp.size(); ++j)
			sang+=temp[j]-'0';
		if(hap[sang]==0 || (hap[sang] != 0 && hap[sang] > sang))
			hap[sang] = i;
	}

	int n;
	scanf("%d",&n);
	printf("%d",hap[n]);
}