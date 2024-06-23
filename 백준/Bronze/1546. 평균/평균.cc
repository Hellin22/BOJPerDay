#include <iostream>
#include <vector>

using namespace std;

int main() {
	int n;
	cin >> n;
	vector<double> v;
	double maxx = -1;
	for (int i = 0; i < n; i++) {
		int a;
		cin >> a;
		v.push_back(a);
		if (maxx < a) maxx = a;
	}

	double summ = 0;
	for (int i = 0; i < n; i++) {
		v[i] = v[i] / maxx * 100;
		summ += v[i];
	}
	cout << summ / n;
}