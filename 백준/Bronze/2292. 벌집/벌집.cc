#include <iostream>

using namespace std;

int main() {
	long long t = 2;
	long long fir = 2; long long sec = 7;
	long long n;
	cin >> n;
	if (n == 1) {
		cout << 1;
		return 0;
	}
	while (1) {
		if (n >= fir && n <= sec) {
			cout << t;
			return 0;
		}
		fir = sec + 1;
		sec = sec + t * 6;
		t++;
	}
}