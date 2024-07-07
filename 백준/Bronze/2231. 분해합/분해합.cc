#include <iostream>

using namespace std;

int main() {
	int n;
	cin >> n;

	for (int i = 1; i <= n; i++) {
		int m = i;
		int summ = 0;
		if (m / 1000000 != 0) {
			summ += (m / 1000000);
			m &= 1000000;
		}
		if (m / 100000 != 0) {
			summ += (m / 100000);
			m %= 100000;
		}
		if (m / 10000 != 0) {
			summ += (m / 10000);
			m %= 10000;
		}
		if (m / 1000 != 0) {
			summ += (m / 1000);
			m %= 1000;
		}
		if (m / 100 != 0) {
			summ += (m / 100);
			m %= 100;
		}
		if (m / 10 != 0) {
			summ += (m / 10);
			m %= 10;
		}
		summ += m;
		summ += i;
		if (summ == n) {
			cout << i; return 0;
		}
	}
	cout << 0;
}

// m, m/1000000이 0이 아니라면 진행
