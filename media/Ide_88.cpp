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
	    ll int arr[n];
	    for(ll int i=0;i<n;i++)
	    {
	        cin>>arr[i];
	    }
	    sort(arr,arr+n);
	    ll int m1=arr[n-1];
	    vector<ll int>v2;
	    set<ll int>s;
	    for(ll int i=0;i<n;i++)
	    {
	        v2.push_back(arr[i]);
	        s.insert(arr[i]);
	    }
	    vector<ll int>v;
	    ll int y=0;
	    for(ll int i=0;i<m1;i++)
	    {
	        if(y==k)
	        {
	            break;
	        }
	        if(!s.count(i))
	        {
	             
	               v.push_back(i);
	               y++;
	         }      
	    }
	   
	    ll int j=0;
	    for(ll int i=0;i<k;i++)
	    {
	        if(y<k)
	        {
	           m1=m1+1;
	           v.push_back(m1+1);
	           v2.push_back((m1+v[j])/2);
	        }
	        else
	        {
	            v2.push_back((m1+v[j])/2);
	        }
	        
	    }
	    map<ll int,ll int>m;
	    ll int o=v2.size();
	    for(ll int i=0;i<o;i++)
	    {
	        m[v2[i]]++;
	    }
	    cout<<m.size()<<endl;
	}
	
   
	return 0;
}
