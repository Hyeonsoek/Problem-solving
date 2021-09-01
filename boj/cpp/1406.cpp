#include <cstdio>
#include <string>
#include <iostream>
#include <stack>
#include <vector>
using namespace std;
stack<char> first,second;

int main()
{
	int N;
	string input;
	cin >> input;
	scanf("%d",&N);
	for(int i=0; i<input.size(); i++)
		first.push(input[i]);
	
	for(int i=0; i<N; i++)
	{
		char temp;
		scanf(" %c",&temp);
		if(temp=='L')
		{
			if(first.empty()) continue;
			else
			{
				second.push(first.top());
				first.pop();
			}
		}
		
		if(temp=='D')
		{
			if(second.empty()) continue;
			else
			{
				first.push(second.top());
				second.pop();
			}
		}
		
		if(temp=='B')
		{
			if(first.empty()) continue;
			else first.pop();
		}
		
		if(temp=='P')
		{
			scanf(" %c",&temp);
			first.push(temp);
		}
	}
	vector<char> f,s;
	while(!first.empty())
	{
		f.push_back(first.top());
		first.pop();
	}
	for(int i=f.size()-1; i>=0; i--)
		cout << f.at(i);
	while(!second.empty())
	{
		printf("%c",second.top());
		second.pop();
	}
}

