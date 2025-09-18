// #include <iostream>
// using namespace std;
// int main() {
//     int x; 
//     cin >> x;
//     bool p1 = x%2 == 0, p2 = x>4 && x<=12;
//     cout << (p1&&p2) << " " << (p1||p2) << " " << (p1!=p2) << " " << (!p1&&!p2);
//     return 0;
// }

#include <iostream>
#include <iomanip>
#include <cstdio>
#include <string>
using namespace std;

int main (){
    double a = 10.11;
    // cout << fixed << setprecision(1) << a << endl;
    string str = "abc";
    printf("%.1f\n", a); // float
    printf("%d\n", 10);
    // cout << str << endl;
    printf("%s", str.c_str());
}