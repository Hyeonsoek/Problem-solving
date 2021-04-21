#include <iostream>
#include <string>
using namespace std;

string croa[8] = {"c=","c-","dz=","d-","lj","nj","s=","z="};

int main()
{
	string str;
	cin >> str;

	int count = 0;
	int size = str.size();
	for(int i=0; i<size; ++i)
	{
		int check = 0;
		for(int j=0; j<8; ++j)
		{
			if(!croa[j].compare(str.substr(i,croa[j].size())))
				{ count++; check = croa[j].size(); break; }
		}

		if(!check)
			count++;
		else
			i+= (check-1);
	}
	cout << count;
}