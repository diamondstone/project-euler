#include <vector>
#include <iostream>
#include <sstream>
#include <cmath>
using namespace std;

vector<int> primesieve(int n){
  vector<int> primes;
  bool prime[n+1];
  prime[0]=prime[1]=false;
  for(int i=2;i<=n;i++){
    prime[i]=true;
  }
  for(int i=2;i<=sqrt(n);i++) {
    if(prime[i]) {
      for(int j = 2*i;j<=n;j+=i) {
        prime[j]=false;
      }
    }
  }
  for(int i=2;i<=n;i++){
    if(prime[i]){primes.push_back(i);}
  }
  return primes;
}

int main() {
  vector<int> primes;
  primes=primesieve(2000000);
  long long sum=0;
  for(vector<int>::iterator it=primes.begin();it!=primes.end();it++){
    sum+=*it;
  }
  cout << sum << endl;
}
