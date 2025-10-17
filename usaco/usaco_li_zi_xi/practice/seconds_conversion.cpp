#include <iostream>
using namespace std;

int main (){
    int seconds ;
    cin >> seconds ;
    cout << seconds / 3600 << "h";
    seconds %= 3600 ;
    cout << seconds << endl;
    cout << seconds / 60 << "min";
    seconds %= 60;
    cout << seconds << "s";
    
    return 0;
}