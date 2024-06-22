#include <iostream>
#include <set>
#include <string>

using namespace std;

set<string> st[51];

int main() {
	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(0);
	int n;
	cin >> n;
	string s;
	

	while (n--) {
		cin >> s;
		int ssize = s.size();
		st[ssize].insert(s);
	}

	for (int i = 0; i < 51; i++) {
		if (st[i].size() != 0) {
			set<string>::iterator it1 = st[i].begin();
			for (it1; it1 != st[i].end(); it1++) {
				cout << *it1 << '\n';
			}
		}
	}
}