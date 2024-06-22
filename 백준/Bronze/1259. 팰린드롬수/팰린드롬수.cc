#include <iostream>
#include <set>
#include <string>
#define FAST  cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);

using namespace std;

int main() {
	FAST;
	string s;
	while (true) {
		cin >> s;
		if (s == "0") break;
		
		int fir = 0;
		int sec = s.size() - 1; // fir이 sec보다 작은 경우만 진행.
		bool flag = true;
		while (fir < sec) {
			if (s[fir] != s[sec]) {
				flag = false;
				cout << "no" << '\n';
				break;
			}
			fir++;
			sec--;
		}
		if (flag) cout << "yes" << '\n';
	}
}