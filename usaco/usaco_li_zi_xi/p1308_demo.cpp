#include <iostream>
using namespace std;

int main()
{
    string input;
    cout << "Enter a line: ";
    getline(cin, input); // 读取一行，包括空格，直到遇到换行符
    cout << tolower('A') << endl;
    cout << "You entered: " << input << endl;
    return 0;
}