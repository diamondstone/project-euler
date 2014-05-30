#include <iostream>
#include <sstream>
#include <cmath>
using namespace std;

long long sumsquares(int n) {
  int total=0;
  for(int i=1;i<=n;i++){
    total+=i*i;
  }
  return total;
}

long long squareofsum(int n) {
  int total=0;
  for(int i=1;i<=n;i++){
    total+=i;
  }
  return total*total;
}

int main() {
  cout << squareofsum(100)-sumsquares(100) << endl;
}
