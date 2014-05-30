


#include <iostream>
#include <cmath>
using namespace std;

int main() {
  double total=0.0;
  int z,s,i;
  double p, probwarm, expected, best;
  double Tcold[10001], Twarm[10001];
  Tcold[0]=0.0;
  Tcold[1]=1.0;
  Twarm[1]=0.0;
  for(z=1;z<51;z++) {
    p=z/100.0;
    cout << "with probability of infection " << p << endl;
    for(s=2;s<10001;s++) {
      best=10000;
      for(i=1;i<s;i++) {
	probwarm=(1.0-pow(1.0-p,i))/(1.0-pow(1.0-p,s));
	expected=1.0+probwarm*(Twarm[i]+Tcold[s-i])+(1.0-probwarm)*Twarm[s-i];
        if(expected<best){best=expected;}
      }
      Twarm[s]=best;
      best=10000;
      for(i=1;i<s+1;i++) {
	expected=1.0+(1.0-pow(1.0-p,i))*Twarm[i]+Tcold[s-i];
        if(expected<best){best=expected;}
      }
      Tcold[s]=best;
    }
    cout << "with 10000 sheep, expected tests is " << Tcold[10000] << endl;
    total+=Tcold[10000];
  }
  cout << "total is " << total << endl;
}
