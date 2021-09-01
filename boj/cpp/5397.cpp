#include <cstdio>
#include <cstring>
#include <stack>
#include <vector>
using namespace std;
int main()
{
	int N,len;
	for(scanf("%d",&N);N--;)
	{
		char input[1000001];
		stack<char> first,second;
		scanf("%s",input);
		len = strlen(input);
		for(int i=0;i<len;i++)
		{
			if(input[i]=='<') {
				if(first.empty()) continue;
				else
				{
					second.push(first.top());
					first.pop();
				}
			}
			
			else if(input[i]=='>') {
				if(second.empty()) continue;
				else
				{
					first.push(second.top());
					second.pop();
				}
			}
			
			else if(input[i]=='-') {
				if(first.empty()) continue;
				else first.pop();
			}
			else first.push(input[i]);
		}
		vector<char> v;
		while(!first.empty())
		{
			v.push_back(first.top());
			first.pop();
		}
		for(int i=v.size()-1; i>=0; i--)
		{
			printf("%c",v.at(i));
		} 
		while(!second.empty())
		{
			printf("%c",second.top());
			second.pop();
		} printf("\n");
	}
}
