#include <iostream>
#include <cmath>
using namespace std;

int main() {
  int p=0;
  int q=1;
  int total=0;
  int t=0;
  while(q<4000000) {
    if(q%2==0){total=total+q;}
    t=p; p=q; q=t+p;
  }
  cout << total << endl;
}
