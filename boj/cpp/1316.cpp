#include <string>
#include <iostream>
#include <vector>
using namespace std;

bool check(string s)
{
	int len = s.size();
	vector<bool> alpha(26,false);

	alpha[s[0]-'a'] = true;
	for(int i=1; i<len; ++i)
	{
		if(s[i] != s[i-1] && alpha[s[i]-'a'])
			return false;

		alpha[s[i]-'a'] = true;
	}
	return true;
}

int main()
{
	int n,count=0;
	cin >> n;
	for(int i=0; i<n; ++i)
	{
		string s;
		cin >> s;
		if(check(s))
			++count;
	}
	cout << count;
}