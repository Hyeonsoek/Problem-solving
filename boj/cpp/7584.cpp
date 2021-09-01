#include <cstdio>
#include <iostream>
#include <string>
using namespace std;
int main() {
	string input;
	getline(cin,input);
	while(input[0]!='#') {
		int x_win=0,o_win=0;
		char map[10] = {};
		int count=1;
		
		if(input[0]=='X') {
			for(int i=2; i<input.size(); i++) {
				if(input[i] >= '1' && input[i] <= '9') {
					if(count%2==1) {
						map[input[i]-'0'] = 'X';
					} else {
						map[input[i]-'0'] = 'O';
					} count++;
				}
			}
		}
		
		if(input[0]=='O') {
			for(int i=2; i<input.size(); i++) {
				if(input[i] >= '1' && input[i] <= '9') {
					if(count%2==1) {
						map[input[i]-'0'] = 'O';
					} else {
						map[input[i]-'0'] = 'X';
					} count++;
				}
			}
		}
		
		for(int j=1; j<4; j++) {
			int x_cnt=0,o_cnt=0;
			for(int i=j; i<10; i+=3) {
				if(map[i]=='O') o_cnt++;
				if(map[i]=='X') x_cnt++;
			}
			if(o_cnt==3) o_win=1;
			if(x_cnt==3) x_win=1;
		}
		for(int i=1; i<10; i+=3) {
			int x_cnt=0,o_cnt=0;
			for(int j=i; j<i+3; j++) {
				if(map[j]=='O') o_cnt++;
				if(map[j]=='X') x_cnt++;
			}
			if(o_cnt==3) o_win=1;
			if(x_cnt==3) x_win=1;
		}
		
		if(map[1]==map[5]&&map[1]==map[9]) {
			if(map[1]=='X') x_win=1;
			if(map[1]=='O') o_win=1;
		}
		
		if(map[3]==map[5]&&map[3]==map[7]) {
			if(map[3]=='X') x_win=1;
			if(map[3]=='O') o_win=1;
		}
		
		if(x_win==0&&o_win==0) printf("Draw\n");
		if(x_win==1) printf("X\n");
		if(o_win==1) printf("O\n");
		getline(cin,input);
	}
}
