#include <iostream>
#include <stack>
#include <vector>
using namespace std;

int main() {
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	stack<int> stck;
	
	int n;
	cin >> n;
	vector<int> v;
	vector<char> v2;
	v.push_back(0);
	int a;
	for (int i = 1; i <= n; i++) {
		cin >> a;
		v.push_back(a);
	}
	int idx = 1; // top이 입력으로 주어진게 아니고 push도 못하면 즉, num > n이면 종료
	int num = 1;
	while (idx <= n) {
		if (stck.empty()) {
			//cout << "push " << num << endl;
			stck.push(num);
			num++;
			v2.push_back('+');
		}
		else {
			if (v[idx] == stck.top()) {
				//cout << "pop " << stck.top() << endl;
				stck.pop();
				idx++;
				v2.push_back('-');
			}
			else if (v[idx] != stck.top()) {
				if (num > n) {
					cout << "NO";
					return 0;
				}
				//cout << "push " << num << endl;
				stck.push(num);
				num++;
				v2.push_back('+');
			}
		}
	}

	for (auto k : v2) {
		cout << k << '\n';
	}
}