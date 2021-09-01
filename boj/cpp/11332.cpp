#include <cstdio>
#define B 100000000
typedef long long int lld;
int main() {
	int N;
	for(scanf("%d",&N);N--;) {
		char input[10]={};
		lld C,T,L,check=0;
		scanf("%s%lld%lld%lld",input,&C,&T,&L);
		if(input[2]=='N'&&input[3]==')') {
			lld IN=0;
			while(IN <= L*B && T > 0) {
				IN += C,T--;
			} if(IN > L*B) check=1;
		}
		if(input[2]=='N'&&input[4]=='2') {
			lld IN=0;
			while(IN <= L*B && T > 0) {
				IN += C*C,T--;
			} if(IN > L*B) check=1;
		}
		if(input[2]=='N'&&input[4]=='3') {
			lld IN=0;
			while(IN <= L*B && T > 0) {
				IN += C*C*C,T--;
			} if(IN > L*B) check=1;
		}
		if(input[2]=='2'&&input[4]=='N') {
			lld IN=T;
			while(IN <= L*B && C > 0) {
				IN *= 2,C--;
			}
			if(IN > L*B)
				check=1;
		}
		if(input[2]=='N'&&input[3]=='!') {
			lld IN=0;
			while(IN <= L*B && T > 0) {
				lld temp=1,NN = C;
				while(temp <= L*B && NN>0) {
					temp *= NN;
					NN--;
				} if(IN <= L*B)
					IN+=temp;
				T--;
			} if(IN > L*B) check=1;
		}
		printf(check==0?"May Pass.\n":"TLE!\n");
	}
}

