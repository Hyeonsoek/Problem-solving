#include <string>
#include <iostream>
using namespace std;

int main()
{
	string input;
	cin >> input;

	int count = 0;
	for(int i=0; i<input.size(); ++i)
	{
		char args = input[i];
		if('A' <= args && args < 'D')
			count+=3;

		if('D' <= args && args < 'G')
			count+=4;

		if('G' <= args && args < 'J')
			count+=5;

		if('J' <= args && args < 'M')
			count+=6;

		if('M' <= args && args < 'P')
			count+=7;

		if('P' <= args && args < 'T')
			count+=8;

		if('T' <= args && args < 'W')
			count+=9;

		if('W' <= args && args <= 'Z')
			count+=10;
	}
	cout << count;
}