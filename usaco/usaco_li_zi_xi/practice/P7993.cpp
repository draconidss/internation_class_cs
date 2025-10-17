#include <iostream>
using namespace std;

int main()
{
    string str;
    cin >> str;
    int sum = 0;
    for (int i = 0; i < str.size() - 2; i++)
    {
        string subStr = str.substr(i, 3);
        if (subStr != "GGG" && subStr != "HHH")
        {
            cout << subStr << endl;
            sum++;
        }
    }
    cout << sum;
    return 0;
}
