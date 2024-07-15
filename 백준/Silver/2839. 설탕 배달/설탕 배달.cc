#include <iostream>

using namespace std;

int main() {
	int N;
	cin >> N;
	bool isMake = true;

	int fiveRemain, threeRemain;
	int fiveQuotient, threeQuotient;
	int Nfive, Nthree;

	fiveRemain = N % 5;
	threeRemain = fiveRemain % 3;
	fiveQuotient = N / 5;
	threeQuotient = (N - (fiveQuotient * 5)) / 3;
	// N이 초기화 되는게 아니라 다른게 초기화됨
	
	Nfive = fiveQuotient * 5 + fiveRemain;
	Nthree = threeQuotient * 3 + threeRemain;

	while (threeRemain != 0) {

		Nfive -= 5;
		Nthree += 5;
		if (Nfive <= 0) {
			isMake = false;
		}

		fiveQuotient = Nfive / 5;
		fiveRemain = Nfive % 5;

		threeQuotient = Nthree / 3;
		threeRemain = Nthree % 3;
	}

	if (isMake == false) cout << -1 << endl;
	else cout << fiveQuotient + threeQuotient << endl;

	// 여기서 문제가 있는게 되는 경우가 여러가지 있을 때 그 중에서 가장 적은수의 봉지를 가져가야함.
	// 그런데 다시 생각해보니까 5키로 봉지가 제일 많을때가 정답이므로 굳이 비교 저장 할필요가 없다.
}
