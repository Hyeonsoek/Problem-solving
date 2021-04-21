#include <cstdio>
#include <string>
using namespace std;
int prime[1400001];

int main() {
	int N;
	scanf("%d",&N);
	for(int i=2; i<=1400000; i++) {
		if(prime[i]==0) {
			if(i>=N) {
				int check = 1;
				string s = to_string(i);
				for(int j=0; j<s.size()/2; j++) {
					if(s[j]!=s[s.size()-j-1]) {
						check=0; break;
					}
				} if (check==1) {
					printf("%d",i);
					return 0;
				}
			}
			for(int j=i*2; j<=1400000; j+=i) {
				prime[j]=1;
			}
		}
	}
}
