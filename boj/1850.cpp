#include <cstdio>
typedef long long ll;
ll gcd(ll a, ll b) {
	return b ? gcd(b, a%b) : a;
}
int main() {
	ll A,B;
	scanf("%lld%lld",&A,&B);
	ll g = gcd(A,B);
	for (ll i = 0; i < g; i++) {
		printf("1");
	}
}
