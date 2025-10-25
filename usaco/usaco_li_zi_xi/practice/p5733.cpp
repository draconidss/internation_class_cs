#include <iostream>
using namespace std;

int main()
{
    string str;
    cin >> str;
    for (char c : str) // char c = str[i]
    {
        if (c >= 'a' && c <= 'z')
        {
            c += 'A' - 'a';
        }
        cout << c;
    }
    return 0;
}