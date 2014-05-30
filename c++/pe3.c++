#include <iostream>
#include <cmath>
using namespace std;

int* factorize(long long n, int* arr) {
  int i;
  int j=0;
  long long r=n;
  for(i=2;i<=sqrt(n);i++){
    while(r%i==0){
      r=r/i;
      arr[j++]=i;
    }
  }
  arr[j]=0;
  return arr;
}



int main() {
  int arr[65];
  factorize(600851475143,arr);
  int j=0;
  while(arr[j]){
    cout << arr[j++] << endl;
  }
}
