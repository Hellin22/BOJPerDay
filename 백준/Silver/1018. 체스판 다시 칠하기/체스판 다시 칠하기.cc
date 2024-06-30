#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

const int MAX = 51;
int chesspan[MAX][MAX];

char case1[8][8] = 
{	{'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', },
	{'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
	{'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
	{'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
	{'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
	{'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
	{'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
	{'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'}};
char case2[8][8]=
{	{'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
	{'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
	{'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
	{'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
	{'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
	{'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
	{'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
	{'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'}};


int main() {
	int maxx = 64;
	
	int N, M; // N, M은 8이상 50이하

	cin >> N >> M;
	string str;
	for (int col = 0; col < N; col++) {
		cin >> str;
		for (int row = 0; row < M; row++) {
			chesspan[col][row] = str[row];
		}
	}
	/*cout << endl;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cout << char(chesspan[i][j]) ;
		}
		cout << endl;
	}*/


	int cnt = 0; int cnt2 = 0;
	for (int i = 0; i <= N - 8; i++) { // 10, 13
		// 0 1 2      0 1 2 3 4 5
		for (int j = 0; j <= M - 8; j++) {
			// 위 크기만큼 반복하는거고 이제 비교할 구문이 필요

			/*for (int row = 0; row < 8; row++) {
				for (int col = 0; col < 8; col++) {

				}
			}*/
			// 반복문 바깥에 있는거는 덜 돌아간다.
			// 따라서 col을 바깥에 적는게 맞다.
			for (int col = i; col < i + 8; col++) {
				for (int row = j; row < j + 8; row++) {
					if (chesspan[col][row] != case1[col - i][row - j]) {
						cnt++;
					}
					if (chesspan[col][row] != case2[col - i][row - j]) {
						cnt2++;
					}
				}
			}


			maxx = min(maxx, min(cnt, cnt2));
			cnt = 0; cnt2 = 0;
		}
	}

	cout << maxx << endl;

}