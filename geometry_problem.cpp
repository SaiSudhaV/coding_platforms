#include <iostream>
using namespace std;
 
int main() {
	int t;
	cin >> t;
	for(int i = 0; i < t; i++){
		long long int a, b, c;
		cin >> a >> b >> c;
		cout << (2 * b) - a - c << endl;
	}
	return 0;
} 