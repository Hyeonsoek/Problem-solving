#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool cmp(const int &a,const int &b)
{ return a > b; }

int main()
{
	string input;
	cin >> input;
	if(input[0] == '0')
	{
		cout << -1; return 0;
	}

	bool inZero = false;
	int sumAll = 0;
	for(int i=0; i<input.size(); ++i)
	{
		if(input[i] == '0')
			inZero = true;
		sumAll += input[i]-'0';
	}
	if(!inZero || sumAll % 3 > 0)
		cout << -1;
	else
	{
		sort(input.begin(),input.end(),cmp);
		cout << input;
	}
}