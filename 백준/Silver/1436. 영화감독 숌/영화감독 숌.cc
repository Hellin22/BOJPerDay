#include <iostream>
#include <string>
using namespace std;

int main() {
	int n;
	int result = 665;
	string temp;
	cin >> n;

	for (int i = 0; i < n; i++) {
		while (1) {
			result++;
			temp = to_string(result);
			if (temp.find("666") != -1)
				break;
		}
	}
	cout << result;
}