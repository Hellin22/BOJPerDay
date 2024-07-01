#include <iostream>
#include <vector>
#include <set>
#define FAST cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);
using namespace std;

int main() {
	FAST;
	int n;
	cin >> n;

	// 1. 입력 수는 십만개 -> 입력 수의 범위는 int 범위 -> 배열로 처리하는건 메모리초과.
	// 2. 십만개이므로 nlogn 시간에 풀어야함. -> log n 시간 안에 원소 존재 유무를 판단할 수 있어야함. -> set으로 하면 됨.
	// 3. set stl을 사용하지 않고 하려면 어떤 방법 사용? -> 
	set<int> st;
	for (int i = 0; i < n; i++) {
		int a;
		cin >> a;
		st.insert(a);
	}
	cin >> n;
	for (int i = 0; i < n; i++) {
		int a;
		cin >> a;
		if (st.find(a) != st.end()) cout << 1 << '\n';
		else cout << 0 << '\n';
	}
}