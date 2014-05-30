#include <iostream>
#include <sstream>
#include <cmath>
using namespace std;

bool ispalindrome(int n) {
  ostringstream oss;
  string s,t;
  oss << n;
  t=s = oss.str();
  reverse(t.begin(),t.end());
  return s==t;
}

int main() {
  int max=0;
  for(int i=100;i<1000;i++){
    for(int j=100;j<1000;j++){
      if(ispalindrome(i*j)&&i*j>max){
        max=i*j;
      }
    }
  }
  cout << max << endl;
}
