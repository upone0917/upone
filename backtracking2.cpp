#include <iostream>
using namespace std;

int arr[8];
bool visited[8];
int N, M;

void Solve(int level)
{
	if (level == M) {
		for (int i = 0; i < M; i++)
			cout << arr[i] << " ";
		cout << '\n';
		return;
	}

	for (int i = 1 ; i <= N; i++) {
		visited[i] = true;
		arr[level] = i;
		Solve(level+1);
		visited[i] = false;
	}
}

int main()
{
	cin >> N >> M;
	Solve(0);
}