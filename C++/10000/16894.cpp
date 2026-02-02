#include <iostream>
constexpr auto MAX = 3500000;
using namespace std;

int main()
{
	long long n; cin >> n;

	if (n == 1)
	{
		cout << "koosaga";
		return 0;
	}

	int count = 0;
	for (int i = 2; i <= MAX && n > 1; i++)
	{
		if (n % i == 0)
		{
			while (n % i == 0)
			{
				n /= i;
				count++;
			}
		}
	}

	if (n > 1) count++;

	cout << ((count == 2) ? "cubelover" : "koosaga");
}