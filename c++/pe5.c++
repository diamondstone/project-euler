#include <iostream>
#include <sstream>
#include <cmath>
using namespace std;

long long gcd(long long n, long long m) {
  if(n*m==0){return n+m;}
  return gcd(m,n%m);
}

long long lcm(long long n, long long m) {
  return n*m/gcd(n,m);
}

long long alldivis(int n) {
  long long p=1;
  for(int i=1;i<=n;i++){
    p=lcm(p,i);
  }
  return p;
}

int main() {
  cout << alldivis(20) << endl;
}
