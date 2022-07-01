#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int N, M;
vector<int> V;
int answer[10];
bool visited[10];

void Solve(int level)
{
	if (level == M) {
		for (int i = 0; i < M; i++)
			cout << answer[i] << " ";
		cout << '\n';
		return;
	}

	for (int i = 0 ; i < V.size() ; i++) {
		if (visited[i])
			continue;
		visited[i] = true;
		answer[level] = V[i];
		Solve(level + 1);
		visited[i] = false;
	}
}

int main()
{
	cin >> N >> M;
	V.resize(N);
	for (int i = 0; i < N; i++)
		cin >> V[i];

	sort(V.begin(), V.end());
	Solve(0);
}