#include <iostream>
using namespace std;

int arr[10];
bool visited[10];
int N, M;

void Solve(int level, int start)
{
	if (level == M) {
		for (int i = 0; i < M; i++)
			cout << arr[i] << " ";
		cout << '\n';
		return;
	}

	for (int i = start; i <= N; i++) {
		visited[i] = true;
		arr[level] = i;
		Solve(level+1, i);
		visited[i] = false;
	}
}

int main()
{
	cin >> N >> M;
	Solve(0, 1);

	return 0;
}
