#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>> n;
    while (n--)
    {
        int a,b;
        cin>>a>>b;
        if ((a+b)%3==0 && (2*min(a,b)>=max(a,b)))
        {
            cout<<"YES"<<endl;
            /* code */
        } else
        {
            cout<<"NO"<<endl;
        }
        
        
        /* code */
    }
    
}