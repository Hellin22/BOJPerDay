#include <iostream>
#include <deque>
#include <algorithm>
#include <string>
#define FAST cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);
using namespace std;

int main() {
	FAST;

	int t;
	cin >> t;
	while (t--) {

		string str;
		cin >> str;
		int ssize;
		cin >> ssize;

		deque<int> dq;

		string v;
		cin >> v;

		for (int i = 1; i < v.size() - 1; i++) {
			string tmp = "";
			if (v[i] != '[' && v[i] != ']' && v[i] != ',') {
				int j = i;
				tmp += v[i];
				while (1) {
					//cout << tmp << " ";
					j++;

					if (v[j] != '[' && v[j] != ']' && v[j] != ',') {
						//cout << v[j] << endl;
						tmp += v[j];
					}
					else {
						i = j - 1;
						break;
					}
					i = j;
				}
				dq.push_back(stoi(tmp));
			}
		}



		bool flag = true;
		int curDir = 1; // 1이면 왼쪽이 front / 0이면 오른쪽이 front

		for (int i = 0; i < str.size(); i++) {
			if (str[i] == 'R') {
				if (dq.empty()) continue;
				if (curDir == 1) curDir = 0;
				else if (curDir == 0) curDir = 1;
			}
			else if (str[i] == 'D') {
				if (dq.empty()) {
					cout << "error" << '\n';
					flag = false;
					break;
				}
				else {
					if (curDir == 1) dq.pop_front();
					else if (curDir == 0) dq.pop_back();
				}
			}
		}

		if (flag) {
			if (dq.empty()) {
				cout << "[]" << '\n';
				continue;
			}
			if (curDir == 1) {
				deque<int>::iterator it1 = dq.begin();
				cout << "[" << *it1;
				it1++;
				if (it1 == dq.end()) cout << "]" << '\n';
				else {
					for (it1; it1 != dq.end(); it1++) {
						cout << "," << *it1;
					}
					cout << "]" << '\n';
				}
			}
			else if (curDir == 0) {
				deque<int>::iterator it1 = dq.end();
				it1--;
				cout << "[" << *it1;
				if (it1 == dq.begin()) cout << "]" << '\n';
				else {
					it1--;
					for (it1; it1 != dq.begin(); it1--) {
						cout << "," << *it1;
					}
					cout << "," << *it1;
					cout << "]" << '\n';
				}
			}
			
			
		}

	}
}