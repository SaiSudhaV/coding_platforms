#include <iostream>
#include <string>
using namespace std;
int main(){
    int n,m,q,x;
    cin>>n>>m;
    string *s=new string [n];
    string *p=new string [m];
    for(int i=0; i<n; i++)
    	cin>>s[i];
    for(int i=0; i<m; i++) 
        cin>>p[i];
    cin>>q;
    while(q--){
    	cin>>x;
    	x--;
    	cout<<s[x%n]<<p[x%m]<<endl;
    }
}
