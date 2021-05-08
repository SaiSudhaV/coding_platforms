#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
using namespace std;
int main() {   
	long n;
	cin >> n;
	long m = n;
	
	map<string, string> phoneBook;
	vector<string> queryName;
	string _name, _phoneNumber;
	while(n--)
	{
		cin >> _name >> _phoneNumber;
		phoneBook.insert(pair<string, string>(_name, _phoneNumber));
	}
	while(m--)
	{
		cin >> _name;
		queryName.push_back(_name);
	}
	for(vector<string>::iterator it = queryName.begin(); it != queryName.end(); ++it)
	{
		map<string, string>::iterator _it = phoneBook.find(*it);
		if( _it != phoneBook.end() )
		{
			cout << _it->first << "=" << _it->second << endl;
		}
		else
		{
			cout << "Not found" << endl;
		}
	}
	return 0;
}
