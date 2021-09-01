#include <cstdio>
/*돌게임 1,2,5 다 이걸로 가능*/
int main() {
	long long stone;
	scanf("%lld",&stone);
	printf("%s",stone%2?"SK":"CY");
}