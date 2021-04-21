#include <iostream>
    #define ll long long
    using namespace std;
    ll t,n,sum,sum1,ans,l,r,x;
    const ll INF=0x3f3f3f3f;
    int main(){
    	cin>>t;
    	while(t--){
    		cin>>n;
    		sum=0,sum1=0,ans=-INF,l=r=1;
    		for(int i=1;i<=n;i++){
    			cin>>x;
    			sum+=x;sum1+=x;
    			if(sum1>ans){
    				ans=sum1;r=i;
    			}
    			if(sum1<=0)  sum1=0,l=i+1;
    		}
    		if(sum<=ans&&!(l==1&&r==n))  puts("NO");
    		else puts("YES");
    	}
    	return 0;
    }