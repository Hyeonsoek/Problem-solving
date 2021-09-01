#include <cstdio>
#include <string>
#include <iostream>
#include <cmath>
using namespace std;
int main(){
	int N;
	scanf("%d",&N);
	for(int i=0;i<N+1;i++){
		string input;
		getline(cin,input);
		int sum=0,len = input.size();
		int x=0,y=0;
		for (int i = 0; i < len; i++) {
			y++;
			if(input[i]==32) {
				string str = input.substr(x,y-x-1);
				x=y;
				int K = 0;
				for (int j = 0; j < str.size(); j++) {
					K += (str[j]-48)*pow(10,str.size()-j-1);
				} sum+=K;
			} if (i == len-1) {
				string str = input.substr(x,len-1);
				int K = 0;
				for (int j = 0; j < str.size(); j++) {
					K += (str[j]-48)*pow(10,str.size()-j-1);
				} sum+=K;
			}
		} if (i>0) printf("%d\n",sum);
	}
}
