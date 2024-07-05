#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

int isprime(int a)
{
	int roota = sqrt((int)a);
	if (a == 1) return 0;
	if (a == 2) return 1;
	else
	{
		for (int i = 2; i <= roota; i++)
		{
			if (a % i == 0) return 0;
		}
	}
	return 1;
}

int main()
{
	int T;
	cin >> T;
	int ressult = 0;
	int a;
	int k = 0; 
	for (int i = 0; i < T; i++)
	{
		cin >> a;
		k = k + isprime(a);
	}
	cout << k << endl;
}