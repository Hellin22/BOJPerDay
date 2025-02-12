#include <iostream>
#include <stack>
#include <vector>
#include <string>

#define FAST cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);

using namespace std;

int main() {
	FAST;
	int cnt = 0;

	string str;
	cin >> str;

	vector<int> idx;
	char a = str[0];
	for (int i = 1; i < str.size(); i++) {
		char b = str[i];
		if (a == '(' && b == ')') {
			idx.push_back(i-1);
		}
		a = b;
	}

	int curIdx = 0;

	stack<int> stck;

	for (int i = 0; i < str.size();) {
		if (curIdx < idx.size() && i == idx[curIdx]) {
			
			curIdx++;
			i += 2;
			cnt += stck.size();
			continue;
		}
		
		if (str[i] == '(') {
			stck.push(1);
		}
		else if (str[i] == ')') {
			stck.pop();
			cnt++;
		}
		i++;
	}
	cout << cnt;
	
}