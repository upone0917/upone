# upone
c++ and python

#최대공약수와 최소공배수
#include <iostream>
using namespace std;

//최대공약수 함수
int GCD(int a, int b)
{
	if (a % b == 0)
		return b;
	else
		return GCD(b, a % b);
}

int main()
{
	int num1, num2;
	cin >> num1 >> num2;

	cout << GCD(num1, num2) << '\n';

	int result = num1 * num2 / GCD(num1, num2); //최소공배수 구하기
	cout << result << endl;
	return 0;
}
