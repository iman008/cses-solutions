#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    long res=1;
    for(int i=0; i<n; i++){
        res=(res*2)%(1000000007);
    }
    cout << res << endl;
    return 0;
}