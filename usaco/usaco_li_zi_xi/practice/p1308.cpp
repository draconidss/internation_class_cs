#include <iostream>
using namespace std;

int main()
{
    string n;
    string check;
    getline(cin, check);
    getline(cin, n);

    cout << check << endl;
    cout << n << endl;

    int sum = 0;
    int pos_first = 0;
    int checking = 0;
    bool flag = false;

    for (int i = 0; i < n.size() - check.size() + 1; ++i)
    {
        if (tolower(n[i]) == tolower(check[1]))
        {
            for (int j = 1; j < check.size(); ++j)
            {
                flag = tolower(n[i + j]) == tolower(check[j]) ? true : false;
            }
            if (flag)
            {
                sum++;
                if (sum == 1)
                {
                    pos_first = i;
                }
            }
            flag = false;
        }
    }
    cout << sum << " " << pos_first;

    return 0;
}