#include <cstdio>
#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main()
{
	stack<char> st;
	string s;

	cin >> s;

	for(int i=0; i<s.size(); ++i)
	{
		if('A' <= s[i] && s[i] <= 'Z')
			printf("%c",s[i]);

		if(s[i] == '(')
			st.push(s[i]);

		if(s[i] == ')')
		{	
			while(st.top()!='(')
			{
				printf("%c",st.top());
				st.pop();
			}
			st.pop();
		}

		if(s[i] == '+' || s[i] == '-')
		{
			while(!st.empty() && st.top()!='(')
			{
				printf("%c",st.top());
				st.pop();
			}
			st.push(s[i]);
		}

		if(s[i] == '*' || s[i] == '/')
		{
			while(!st.empty() && (st.top()=='*'||st.top()=='/'))
			{
				printf("%c",st.top());
				st.pop();
			}
			st.push(s[i]);
		}
	}

	while(!st.empty())
	{
		printf("%c",st.top());
		st.pop();
	}
}