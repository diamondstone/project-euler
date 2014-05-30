#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

vector<int> pytriplesum(int total) {
  int c;
  vector<int> trip;
  for(int a=1;a<total;a++){
    for(int b=a;b<total-a;b++){
      c=total-a-b;
      if(a*a+b*b==c*c){
        trip.push_back(a);trip.push_back(b);trip.push_back(c);
        return trip;
      }
    }
  }
}

int main() {
  vector<int> trip;
  trip=pytriplesum(1000);
  cout << trip[0]*trip[1]*trip[2] << endl;
}
