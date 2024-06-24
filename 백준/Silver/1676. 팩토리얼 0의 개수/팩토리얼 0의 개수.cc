#include <iostream>

using namespace std;

int main() {
	int n;
	cin >> n;

	// n! 에서 처음 0이 아닌 숫자가 나올 때 까지의 0의 개수를 구하기
	// 이 말은 *10이 얼마나 들어가있는지를 구하는 문제.

	int twoes = 0;
	int fives = 0;
	for (int fir = 1; fir <= n; fir++) {
		int tmp = fir;
		while (1) {
			if (tmp % 2 == 0) {
				tmp /= 2;
				twoes++;
				continue;
			}
			else if (tmp % 5 == 0) {
				tmp /= 5;
				fives++;
				continue;
			}
			break;
		}
	}
	cout << min(twoes, fives);
}