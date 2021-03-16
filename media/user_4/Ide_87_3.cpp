#include <bits/stdc++.h>
using namespace std;
#define M1 1000000007
#define M2 998244353
#define INF 1e18
#define ll long long
#define pll pair<ll,ll>
#define REP(i,a,b) for(ll i=a;i<b;i++)
#define REPR(i,a,b) for(ll i=b-1;i>=a;i--)
#define forr(i,n) for(ll i=0;i<n;i++)
#define F first
#define S second
#define pb push_back
#define DB pop_back
#define mp make_pair
#define MT make_tuple
#define V(a) vector<a>
#define vi vector<int>
#define vlli vector <long long>
#define endl '\n'
#define ce(ele) cout<<ele<<' '
#define cs(ele) cout<<ele<<'\n'
#define CASE(t) ll t; cin>>t; while(t--)
/********************************************************************/
const double pi = 3.1415926535;
/********************************************************************/
//FAST IO//
void FAST() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
}
/********************************************************************/
ll int gcd(ll int a,ll int b)
{
    if (b == 0)
        return a;
    return gcd(b, a % b); 
     
}
ll int power2(ll int n)
{
    ll int ok=1;
    while(n>0)
    {
        ok=1;
        if(n%2==0)
        {
            n=n/2;
            ok=0;
            if(n==1)
            {
                break;
            }
        }
        else
        {
            break;
            
        }
    }
    if(ok==0)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int main() {
	// your code goes here
	FAST();
	CASE(t)
	{
	    ll int n,k;
	    cin>>n>>k;
	    string s;
	    cin>>s;
	    if(k==0)
	    {
	        cout<<"YES"<<endl;
	    }
	    else if(2*k==n)
	    {
	        cout<<"NO"<<endl;
	    }
	    else 
	    {
	        ll int ok=0;
	        for(ll int i=0;i<k;i++)
	        {
	            if(s[i]!=s[n-i-1])
	            {
	                ok=1;
	                break;
	            }
	        }
	        if(ok==0)
	        {
	            cout<<"YES"<<endl;
	        }
	        else
	        {
	            cout<<"NO"<<endl;
	        }
	    }
	    
	}
	
   
	return 0;
}
