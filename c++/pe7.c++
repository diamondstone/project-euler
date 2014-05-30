#include <iostream>
#include <sstream>
#include <cmath>
using namespace std;

bool* primesieve(bool* arraystart, int n) {
  *arraystart=*(arraystart+1)=false;
  for(int i=2;i<=n;i++){
    *(arraystart+i)=true;
  }
  for(int i=2;i<=sqrt(n);i++) {
    if(*(arraystart+i)) {
      for(int j = 2*i;j<=n;j+=i) {
        *(arraystart+j)=false;
      }
    }
  }
}

int main() {
  int n=200000;
  int target=10001;
  int count=0;
  bool prime[n+1];
  bool* arraystart=prime;
  primesieve(arraystart,n);
  int i=0;
  while(count<target){
      if(prime[++i]){count++;}
  }
  cout << i << endl;
}
