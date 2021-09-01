#include <iostream>
#include <string>
using namespace std;
int main()
{
	string s;
	string first = "`1234567890-=";
	string second = "QWERTYUIOP[]\\";
	string third = "ASDFGHJKL;'"; 
	string fourth = "ZXCVBNM,./";
	while(getline(cin,s))
	{
		for(int i=0; i<s.size(); i++)
		{
			int f=0,se=0,t=0,ft=0;
			
			for(int j=0; j<13; j++)
			{
				if(s[i]==first[j]) f=j;
				if(s[i]==second[j]) se=j;
				if(j<11&&s[i]==third[j]) t=j;
				if(j<10&&s[i]==fourth[j]) ft=j;
			}
			
			if(f>0) s[i]=first[f-1];
			if(se>0) s[i]=second[se-1];
			if(t>0) s[i]=third[t-1];
			if(ft>0) s[i]=fourth[ft-1];
		}
		
		cout << s << '\n';
	}
}
