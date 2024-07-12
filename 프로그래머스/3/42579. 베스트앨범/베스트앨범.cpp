#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <set>
using namespace std;

bool compare(pair<int, int> cntidx1, pair<int, int> cntidx2) {
	if (cntidx1.first == cntidx2.first) {
		return cntidx1.second < cntidx2.second;
	}
	else {
		return cntidx1.first > cntidx2.first;
	}
}


vector<int> solution(vector<string> genres, vector<int> plays) {
	unordered_map<string, int> unmp;
    vector<int> results;
    
    for (int i = 0; i < genres.size(); i++) {
		unmp[genres[i]] += plays[i];
	}
	
	unordered_map<string, int>::iterator it1 = unmp.begin();
	
	vector<pair<int, string>> playcntNameVector;
	for (it1; it1 != unmp.end(); it1++) {
		playcntNameVector.push_back({ it1->second, it1->first });
	}

	sort(playcntNameVector.begin(), playcntNameVector.end(), greater<pair<int, string>>());
	// 나오는건 이게 나옴. palycnt[1] = {재생수, 클래식) // 높은게 먼저 나옴.

	unordered_map<string, int> nameIdx;
	for (int i = 0; i < playcntNameVector.size(); i++) {
		nameIdx[playcntNameVector[i].second] = i;
	} // nameIdx[클래식] = 0번 이런식으로 idx가 나오게됨.
	// set을 넣어볼까?
	vector<vector<pair<int, int>>> cntIdx(nameIdx.size());

	for (int i = 0; i < plays.size(); i++) {
		string musicName = genres[i];
		int ccnt = plays[i];
		
		cntIdx[nameIdx[musicName]].push_back({ ccnt, i });
	}
	for (int i = 0; i < cntIdx.size(); i++) {
		sort(cntIdx[i].begin(), cntIdx[i].end(), compare);
	}

	for (int i = 0; i < cntIdx.size(); i++) {
		if (cntIdx[i].size() == 1) {
			results.push_back(cntIdx[i][0].second);
		}
		else {
			results.push_back(cntIdx[i][0].second);
			results.push_back(cntIdx[i][1].second);
		}
    }
    
    
    return results;
}
