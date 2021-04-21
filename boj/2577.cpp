#include <cstdio>
#include <cstring>
#include <string>
using namespace std;
int main() {
	int A,B,C,Var[11] = {};
	scanf("%d%d%d",&A,&B,&C);
	int mult = A*B*C,len;
	string Input = to_string(mult);
	len = Input.size();
	for (int i = 0; i < len; i++) {
		Var[Input[i]-'0']++;
	}
	for (int i = 0; i < 10; i++) {
		printf("%d\n",Var[i]);
	}
}
