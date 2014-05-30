#include <iostream>
#include <cmath>
using namespace std;

int main() {
  int z=0;
  int total=0;
  for(z=1;z<1000;z++) {
    if(z%3==0||z%5==0){total=total+z;}
  }
  cout << total << endl;
}
